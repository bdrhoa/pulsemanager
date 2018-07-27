#import random
import base64
#import json
from datetime import datetime
import pandas as pd
#import pulsemanager.lsrc3 as lsrc2
import os
import logging
import io
import boto3

import environ

from pulsemanager.users import models as user_models

from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

env = environ.Env()

LS_URL = env('PULSESERVER')
LS_USERNAME = env('PULSEMGRUSER')
LS_PASSWORD = env('PULSEMGRPSWD')
LS_BASESURVEY_ID = 77736
STATIC_URL = settings.STATIC_URL
ISPROD = True if settings.ENVIRONMENT == "PROD" else False

#ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['pulse.tycp.online', ])

class Survey(models.Model):

    '''The Django Survey Model'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    surveyid = models.IntegerField(_('Survey ID'), primary_key=True, default=0)
    surveyname = models.CharField(_('Name of Survey'), blank=True,
        max_length=255, default='surveyname')
    issurveyactive = models.BooleanField(_('Is Survey Active'), default=True)
    user = models.ForeignKey(user_models.User,
            related_name='surveys',
            on_delete=models.DO_NOTHING,)

    def __str__(self):
        return self.surveyname

    def get_absolute_url(self):
        return reverse('survyes:detail', kwargs={'surveyname': self.surveyname})


    def copy_limesurvey(self):
        ''' Make a copy of survey LS_BASESURVEY_ID '''

        import pulsemanager.lsrc3.session as lsrc

        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.ERROR)

        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)

        self.surveyname = self.user.username + " - " + datetime.now().isoformat()
        self.surveyid = lssession.copy_survey(LS_BASESURVEY_ID, self.surveyname)
        logger.debug('surveyid: %s',self.surveyid)
        self.issurveyactive = True
        lssession.activate_survey(self.surveyid)
        lssession.close()

    def expire(self):
        ''' Set the survey expire date. '''

        import pulsemanager.lsrc3.session as lsrc

        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)
        lssession.expire_survey(self.surveyid)
        lssession.close()

    def _get_ls_data(self):
        '''Get the survey raw data from limesurvey'''

        import pulsemanager.lsrc3.session as lsrc
        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)
        data = lssession.export_responses(self.surveyid)
        lssession.close()
        return data


    def get_data(self):
        '''Get the final survey data'''

        data = self._get_ls_data()

        try:
            sdata= base64.b64decode(data[0])
        except:
            return pd.DataFrame({'A' : []}) #empty

        df = pd.read_csv(io.StringIO(sdata.decode('utf-8')),sep=';')

        df['q1tot'] =  df['q1[vis1]'] + df['q1[vis2]'] + df['q1[vis3]'] + \
            df['q1[vis4]'] + df['q1[vis5]'] + df['q1[vis6]'] + df['q1[vis7]']

        df['q2tot'] = df['q2[lea1]'] + df['q2[lea2]'] + df['q2[lea3]'] + \
            df['q2[lea4]'] + df['q2[lea5]'] + df['q2[lea6]'] + df['q2[lea7]']

        df['q3tot'] = df['q3[bod1]'] + df['q3[bod2]'] + df['q3[bod3]'] + \
             df['q3[bod4]'] + df['q3[bod5]'] +  df['q3[bod6]'] + df['q3[bod7]']

        df['q4tot'] = df['q4[res1]'] +  df['q4[res2]'] + df['q4[res3]'] + \
            df['q4[res4]'] + df['q4[res5]'] + df['q4[res6]'] + df['q4[res7]']

        df['q5tot'] = df['q5[con1]'] + df['q5[con2]'] + df['q5[con3]'] + \
            df['q5[con4]'] + df['q5[con5]'] + df['q5[con6]'] + df['q5[con7]']

        df['q6tot'] = df['q6[eva1]'] + df['q6[eva2]'] + df['q6[eva3]'] + \
             df['q6[eva4]'] + df['q6[eva5]'] + df['q6[eva6]'] +  df['q6[eva7]']

        df['q7tot'] = df['q7[edu1]'] + df['q7[edu2]'] + df['q7[edu3]'] + \
             df['q7[edu4]'] + df['q7[edu5]'] + df['q7[edu6]'] + df['q7[edu7]']

        df['q8tot'] = df['q8[ser1]'] + df['q8[ser2]'] + df['q8[ser3]'] + \
             df['q8[ser4]'] + df['q8[ser5]']  + df['q8[ser6]'] + df['q8[ser7]']

        df['q9tot'] = df['q9[fel1]'] + df['q9[fel2]'] + df['q9[fel3]'] + \
             df['q9[fel4]'] + df['q9[fel5]'] + df['q9[fel6]'] + df['q9[fel7]']

        df['q10tot'] = df['q10[wor1]'] + df['q10[wor2]'] + df['q10[wor3]'] + \
            df['q10[wor4]'] + df['q10[wor5]'] + df['q10[wor6]'] +  df['q10[wor7]']

        #Get rid of non-numeric fields.
        df = df.drop(['id', 'lastpage', 'seed', 'AgeGroup', 'Gender', \
         'Race', 'MinistryRole'], axis = 1)

        means = df.mean(axis = 0, numeric_only = True)
        means['responses'] = len(df)

        return means

    def autolabel(self,rects, ax):

        #Attach a text label above each bar displaying its height

        #Because the values of the bar chart are passed in as
        # (value -1), we must increase the height by 1 to get the
        # correct label value. Then we have to take (height -1) to
        # correct label position.

        for rect in rects:
            height = rect.get_height() + 1
            ax.text(rect.get_x() + rect.get_width()/2., 1.005*(height -1),
                    '%2.2f' % height,
                    ha='center', va='bottom')


    def barchart(self, categories, values, title, xlabel, ylabel):
        # Plots a box chart.

        # Note that the chart is labeled 1 to 10, but the 1 is at
        # the 0 position. So each actual value must be passed in as
        # (value -1).
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.colors
        from pylab import arange

        index = np.arange(len(categories))
        fig, ax = plt.subplots()
        rects1 = ax.bar(index, values, color='cyan')
        plt.axhline(6, color="green", linewidth=5)
        plt.axhline(2, color="red", linewidth=5)
        plt.xlabel(_(xlabel), fontsize=5)
        plt.ylabel(_(ylabel), fontsize=5)
        plt.xticks(index, categories, fontsize=5, rotation=30)
        pos = arange(10)+.05
        plt.yticks(pos,( '1','2','3','4','5','6','7','8','9','10'))
        plt.title(_(title))
        self.autolabel(rects1, ax)

        #files names always use english
        png_name = "{surveyid}_{title}.png".format(surveyid =self.surveyid,
                        title=title.lower())
        #TODO: use djang_storages instead of boto3 directly
        if ISPROD:
            png_name = "static/images/{key}".format(key=png_name)
            img_data = io.BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            s3 = boto3.resource('s3',
                aws_access_key_id=env("DJANGO_AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=env("DJANGO_AWS_SECRET_ACCESS_KEY"))
            bucket = s3.Bucket(env("DJANGO_AWS_STORAGE_BUCKET_NAME"))
            bucket.put_object(Body=img_data, ContentType='image/png', Key=png_name)
            object_acl = s3.ObjectAcl(env("DJANGO_AWS_STORAGE_BUCKET_NAME"),png_name)
            response = object_acl.put(ACL='public-read')
        else:
            fileName = "pulsemanager/static/images/{key}".format(key=png_name)
            plt.savefig(fileName, bbox_inches='tight')

        plt.close('all')

    def radargraph(self,cat, values):
        # Plots a radar chart.

        from math import pi
        import matplotlib.pyplot as plt
        import numpy as np

        N = len(cat)

        x_as = [n / float(N) * 2 * pi for n in range(N)]

        # Because our chart will be circular we need to append a copy of the first
        # value of each list at the end of each list with data
        values += values[:1]
        x_as += x_as[:1]


        # Set color of axes
        plt.rc('axes', linewidth=0.5, edgecolor="#888888")


        # Create polar plot
        ax = plt.subplot(111, polar=True)


        # Set clockwise rotation. That is:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)


        # Set position of y-labels
        ax.set_rlabel_position(0)


        # Set color and linestyle of grid
        ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
        ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)


        # Set number of radial axes and remove labels
        plt.xticks(x_as[:-1], [])

        # Set yticks
        plt.yticks([20, 40, 60, 80, 100], ["2", "4", "6", "8", "10"])

        # Plot data
        ax.plot(x_as, values, linewidth=0, linestyle='solid', zorder=3)

        # Fill area
        ax.fill(x_as, values, 'b', alpha=0.3, color='cyan')


        # Set axes limits
        plt.ylim(0, 100)


        # Draw ytick labels to make sure they fit properly
        for i in range(N):
            angle_rad = i / float(N) * 2 * pi

            if angle_rad == 0:
                ha, distance_ax = "center", 10
            elif 0 < angle_rad < pi:
                ha, distance_ax = "left", 1
            elif angle_rad == pi:
                ha, distance_ax = "center", 1
            else:
                ha, distance_ax = "right", 1

            ax.text(angle_rad, 100 + distance_ax, cat[i], size=10, horizontalalignment=ha, verticalalignment="center")

        #Add thresholds
        HIGHT = 70
        LOWT = 30
        ax.plot(np.linspace(0, 2*np.pi, 100), np.ones(100)*HIGHT, c='g', ls='--')
        ax.plot(np.linspace(0, 2*np.pi, 100), np.ones(100)*LOWT, c='r', ls='--')

        png_name = "{surveyid}_radar.png".format(surveyid =self.surveyid)

        if ISPROD:
            png_name = "static/images/{key}".format(key=png_name)
            img_data = io.BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            s3 = boto3.resource('s3',
                aws_access_key_id=env("DJANGO_AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=env("DJANGO_AWS_SECRET_ACCESS_KEY"))
            bucket = s3.Bucket(env("DJANGO_AWS_STORAGE_BUCKET_NAME"))
            bucket.put_object(Body=img_data, ContentType='image/png', Key=png_name)
            object_acl = s3.ObjectAcl(env("DJANGO_AWS_STORAGE_BUCKET_NAME"),png_name)
            response = object_acl.put(ACL='public-read')
        else:
            fileName = "pulsemanager/static/images/{key}".format(key=png_name)
            plt.savefig(fileName, bbox_inches='tight')

        plt.close('all')

    def createreport(self):
        '''Create the PDF report for the church'''
        import matplotlib
        matplotlib.use('Agg')
        reportdata = self.get_data()

        if  reportdata.empty:
            return reportdata

        categories = ['1','2','3','4','5','6','7']

        x_value_label = 'Question'
        y_value_label = 'Average'

        try:
            #VISION
            barchartdata = [reportdata['q1[vis1]'] -1, reportdata['q1[vis2]'] -1, reportdata['q1[vis3]'] -1,
                reportdata['q1[vis4]'] -1, reportdata['q1[vis5]'] -1, reportdata['q1[vis6]'] -1,
                reportdata['q1[vis7]'] -1]

            chart_title = 'VISION'

            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #LEADERSHIP
            barchartdata = [reportdata['q2[lea1]'] -1, reportdata['q2[lea2]'] -1, reportdata['q2[lea3]'] -1,
                reportdata['q2[lea4]'] -1, reportdata['q2[lea5]'] -1, reportdata['q2[lea6]'] -1,
                reportdata['q2[lea7]'] -1]

            chart_title = 'LEADERSHIP'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)


            #MOBILIZATION
            barchartdata = [reportdata['q3[bod1]'] -1, reportdata['q3[bod2]'] -1, reportdata['q3[bod3]'] -1,
                reportdata['q3[bod4]'] -1, reportdata['q3[bod5]'] -1, reportdata['q3[bod6]'] -1,
                reportdata['q3[bod7]'] -1]

            chart_title = 'MOBILIZATION'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #STEWARDSHIP
            barchartdata = [reportdata['q4[res1]'] -1, reportdata['q4[res2]'] -1, reportdata['q4[res3]'] -1,
                reportdata['q4[res4]'] -1, reportdata['q4[res5]'] -1, reportdata['q4[res6]'] -1,
                reportdata['q4[res7]'] -1]

            chart_title = 'STEWARDSHIP'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #CONTEXT
            barchartdata = [reportdata['q5[con1]'] -1, reportdata['q5[con2]'] -1, reportdata['q5[con3]'] -1,
                reportdata['q5[con4]'] -1, reportdata['q5[con5]'] -1, reportdata['q5[con6]'] -1,
                reportdata['q5[con7]'] -1]

            chart_title = 'CONTEXT'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #EVANGELISM
            barchartdata = [reportdata['q6[eva1]'] -1, reportdata['q6[eva2]'] -1, reportdata['q6[eva3]'] -1,
                reportdata['q6[eva4]'] -1, reportdata['q6[eva5]'] -1, reportdata['q6[eva6]'] -1,
                reportdata['q6[eva7]'] -1]

            chart_title = 'EVANGELISM'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #DISCIPLESHIP
            barchartdata = [reportdata['q7[edu1]'] -1, reportdata['q7[edu2]'] -1, reportdata['q7[edu3]'] -1,
                reportdata['q7[edu4]'] -1, reportdata['q7[edu5]'] -1, reportdata['q7[edu6]'] -1,
                reportdata['q7[edu7]'] -1]

            chart_title = 'DISCIPLESHIP'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #SERVICE
            barchartdata = [reportdata['q8[ser1]'] -1, reportdata['q8[ser2]'] -1, reportdata['q8[ser3]'] -1,
                reportdata['q8[ser4]'] -1, reportdata['q8[ser5]'] -1, reportdata['q8[ser6]'] -1,
                reportdata['q8[ser7]'] -1]

            chart_title = 'SERVICE'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #FELLOWSHIP
            barchartdata = [reportdata['q9[fel1]'] -1, reportdata['q9[fel2]'] -1, reportdata['q9[fel3]'] -1,
                reportdata['q9[fel4]'] -1, reportdata['q9[fel5]'] -1, reportdata['q9[fel6]'] -1,
                reportdata['q9[fel7]'] -1]

            chart_title = 'FELLOWSHIP'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #WORSHIP
            barchartdata = [reportdata['q10[wor1]'] -1, reportdata['q10[wor2]'] -1, reportdata['q10[wor3]'] -1,
                reportdata['q10[wor4]'] -1, reportdata['q10[wor5]'] -1, reportdata['q10[wor6]'] -1,
                reportdata['q10[wor7]'] -1]

            chart_title = 'WORSHIP'
            self.barchart(categories, barchartdata, chart_title, x_value_label, y_value_label)

            #CATEGORY
            categories = [_('Vision'),_('Leadership'),_('Mobilization'), \
            _('Stewardship'),_('Context'),_('Evangelism'),_('Discipleship'), \
            _('Service'),_('Fellowship'),_('Worship')]

            barchartdata = [reportdata['q1tot']/7 -1, reportdata['q2tot']/7 -1, \
                        reportdata['q3tot']/7 -1, reportdata['q4tot']/7 -1, \
                        reportdata['q5tot']/7 -1, reportdata['q6tot']/7 -1, \
                        reportdata['q7tot']/7 -1, reportdata['q8tot']/7 -1, \
                        reportdata['q9tot']/7 -1, reportdata['q10tot']/7 -1]

            self.barchart(categories, barchartdata, _('CATEGORY'), "", _('Average'))

            #RADAR CHART
             # normalize the data based on a max of 70 possilbe "points". This makes the graph spread accross 5 groups of 20

            radardata = [int(round(reportdata['q1tot']/70*100,0)), int(round(reportdata['q2tot']/70*100,0)), \
                int(round(reportdata['q3tot']/70*100,0)), int(round(reportdata['q4tot']/70*100,0)), \
                int(round(reportdata['q5tot']/70*100,0)), int(round(reportdata['q6tot']/70*100,0)), \
                int(round(reportdata['q7tot']/70*100,0)), int(round(reportdata['q8tot']/70*100,0)), \
                int(round(reportdata['q9tot']/70*100,0)), int(round(reportdata['q10tot']/70*100,0))]

            self.radargraph(categories, radardata)
        except:
            reportdata = pd.DataFrame({'A' : []}) #empty
        return reportdata
