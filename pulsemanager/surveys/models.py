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
    
    def add_total(self, therecord):
        '''Add category totals.'''
        q1tot = therecord[0] + therecord[1]+ therecord[2]+ therecord[3]+ therecord[4]+ therecord[5]+ therecord[6]
        q2tot = therecord[7] + therecord[8]+ therecord[9]+ therecord[10]+ therecord[11]+ therecord[12]+ therecord[13]
        q3tot = therecord[14] + therecord[15]+ therecord[16]+ therecord[17]+ therecord[18] + therecord[19] + therecord[20]
        q4tot = therecord[21]+ therecord[22]+ therecord[23]+ therecord[24]+ therecord[25]+ therecord[26] + therecord[27]
        q5tot = therecord[28]+ therecord[29]+ therecord[30]+ therecord[31]+ therecord[32]+ therecord[33] + therecord[34]
        q6tot = therecord[35]+ therecord[36]+ therecord[37]+ therecord[38]+ therecord[39]+ therecord[40] + therecord[41]
        q7tot = therecord[42]+ therecord[43]+ therecord[44]+ therecord[45]+ therecord[46]+ therecord[47] + therecord[48]
        q8tot = therecord[49]+ therecord[50]+ therecord[51]+ therecord[52]+ therecord[53]+ therecord[54] + therecord[55]
        q9tot = therecord[56]+ therecord[57]+ therecord[58]+ therecord[59]+ therecord[60]+ therecord[61] + therecord[62]
        q10tot = therecord[63]+ therecord[64]+ therecord[65]+ therecord[66]+ therecord[67]+ therecord[68] + therecord[69]

        return [q1tot, q2tot, q3tot, q4tot, q5tot, q6tot, q7tot, q8tot, q9tot, q10tot]
    
    def get_data(self):
        '''Get the survey data from limesurvey'''

        import pulsemanager.lsrc3.session as lsrc

        lssession = lsrc.Session(LS_URL, LS_USERNAME, LS_PASSWORD)
 
        data = lssession.export_responses(self.surveyid)
        #data = lssession.export_responses(sid)
        sdata= base64.b64decode(data[0]) 
        df = pd.read_csv(io.StringIO(sdata.decode('utf-8')),sep=';')
        df[['q1tot', 'q2tot', 'q3tot', 'q4tot', 'q5tot', 
           'q6tot', 'q7tot', 'q8tot', 'q9tot', 'q10tot']] = \
            df[['q1[vis1]',
        'q1[vis2]', 'q1[vis3]', 'q1[vis4]', 'q1[vis5]', 'q1[vis6]', 'q1[vis7]',
        'q2[lea1]', 'q2[lea2]', 'q2[lea3]', 'q2[lea4]', 'q2[lea5]', 'q2[lea6]',
        'q2[lea7]', 'q3[bod1]', 'q3[bod2]', 'q3[bod3]', 'q3[bod4]', 'q3[bod5]',
        'q3[bod6]', 'q3[bod7]', 'q4[res1]', 'q4[res2]', 'q4[res3]', 'q4[res4]',
        'q4[res5]', 'q4[res6]', 'q4[res7]', 'q5[con1]', 'q5[con2]', 'q5[con3]',
        'q5[con4]', 'q5[con5]', 'q5[con6]', 'q5[con7]', 'q6[eva1]', 'q6[eva2]',
        'q6[eva3]', 'q6[eva4]', 'q6[eva5]', 'q6[eva6]', 'q6[eva7]', 'q7[edu1]',
        'q7[edu2]', 'q7[edu3]', 'q7[edu4]', 'q7[edu5]', 'q7[edu6]', 'q7[edu7]',
        'q8[ser1]', 'q8[ser2]', 'q8[ser3]', 'q8[ser4]', 'q8[ser5]', 'q8[ser6]',
        'q8[ser7]', 'q9[fel1]', 'q9[fel2]', 'q9[fel3]', 'q9[fel4]', 'q9[fel5]',
        'q9[fel6]', 'q9[fel7]', 'q10[wor1]', 'q10[wor2]', 'q10[wor3]', \
        'q10[wor4]', 'q10[wor5]', 'q10[wor6]', 'q10[wor7]']].apply(self.add_total,axis=1,reduce=None)

        lssession.close()

        return df

    def createreport(self):
        '''Create the PDF report for the church'''
        df = self.get_data()
        return df
