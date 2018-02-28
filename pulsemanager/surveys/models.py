#import random
import base64
#import json
from datetime import datetime
import pandas as pd
#import pulsemanager.lsrc3 as lsrc2
import os
import logging
import io

from pulsemanager.users import models as user_models

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


LS_URL = os.environ["PULSESERVER"]
LS_USERNAME = os.environ["PULSEMGRUSER"]
LS_PASSWORD = os.environ["PULSEMGRPSWD"]
LS_BASESURVEY_ID = 77736 

class Survey(models.Model):
   
    '''The Django Survey Model'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    surveyid = models.IntegerField(_('Survey ID'), primary_key=True, default=0)
    surveyname = models.CharField(_('Name of Survey'), blank=True, max_length=255)
    issurveyactive = models.BooleanField(_('Is Survey Active'), default=True)
    user = models.ForeignKey(user_models.User, related_name='surveys')

    def __str__(self):
        return self.surveyname

    def get_absolute_url(self):
        return reverse('survyes:detail', kwargs={'surveyname': self.surveyname})

    
    def copy_limesurvey(self):
        ''' Copy the base Limesurvey survey and return the new id and name.
            just stubbed for now '''
        
        import pulsemanager.lsrc3.session as lsrc

        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        
        logger.debug('*** start copy_limesurvey ***')
        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)
        logger.debug('**********WE HAVE A SESSION*************')
        logger.debug('sessionid: %s',lssession)
        #TODO decativate existing survey if one exists
            #list survey by user with expired = none
            #set expired = datetime.now().isoformat()

        #self.surveyid = random.randint(1000, 9999)
        self.surveyname = self.user.username + " - " + datetime.now().isoformat()
        self.surveyid = lssession.copy_survey(LS_BASESURVEY_ID, self.surveyname)
        logger.debug('surveyid: %s',self.surveyid)
        self.issurveyactive = True
        lssession.activate_survey(self.surveyid)
        lssession.close()
        logger.debug('*** end copy_limesurvey ***')

    def expire(self):
        ''' Set the survey expire date. '''
    
        import pulsemanager.lsrc3.session as lsrc

        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)
        lssession.expire_survey(self.surveyid)
        lssession.close()
        
    def get_data(self):
        '''Get the survey data from limesurvey'''

        import pulsemanager.lsrc3.session as lsrc

        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)
 
        data = lssession.export_responses(self.surveyid)
        #data = lssession.export_responses(sid)
        sdata= base64.b64decode(data[0]) 
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

        lssession.close()

        #Get rid of non-numeric fields.
        df = df.drop(['id', 'lastpage', 'seed', 'Country', 'lang', 'AgeGroup', 'Gender', \
         'Race', 'MinistryRole'], axis = 1)

        means = df.mean(axis = 0, numeric_only = True)
        means['responses'] = len(df)

        return means

    def createreport(self):
        '''Create the PDF report for the church'''
        reportdata = self.get_data()
        return reportdata
