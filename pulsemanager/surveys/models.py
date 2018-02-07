#import random
#import base64
#import json
from datetime import datetime
#import pandas as pd
#import pulsemanager.lsrc3 as lsrc2

import logging

from pulsemanager.users import models as user_models

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _



LS_DEMO_URL = 'https://lsdemo.limequery.com/admin/remotecontrol'
LS_DEMO_USERNAME = 'limedemo'
LS_DEMO_PASSWORD = 'demo'
LS_DEMO_BASESURVEY_ID =519893

LS_DEMO_URL = 'http://page2voice.com/pulse/index.php/admin/remotecontrol'
LS_DEMO_USERNAME = 'pulse'
LS_DEMO_PASSWORD = 'PdmswOAfh9PY'
LS_DEMO_BASESURVEY_ID = 535175 

LS_DEMO_NEW_SURVEY_NAME = "Copy of Base Survey"

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
        lssession = lsrc.Session(LS_DEMO_URL, LS_DEMO_USERNAME, LS_DEMO_PASSWORD)
        logger.debug('**********WE HAVE A SESSION*************')
        logger.debug('sessionid: %s',lssession)
        #TODO decativate existing survey if one exists
            #list survey by user with expired = none
            #set expired = datetime.now().isoformat()

        #self.surveyid = random.randint(1000, 9999)
        self.surveyname = self.user.username + " - " + datetime.now().isoformat()
        self.surveyid = lssession.copy_survey(LS_DEMO_BASESURVEY_ID, self.surveyname)
        logger.debug('surveyid: %s',self.surveyid)
        self.issurveyactive = True
        lssession.activate_survey(self.surveyid)
        lssession.close()
        logger.debug('*** end copy_limesurvey ***')

    def expire(self):
        ''' Copy the base Limesurvey survey and return the new id and name.
        just stubbed for now '''
    
        import pulsemanager.lsrc3.session as lsrc

        lssession = lsrc.Session(LS_DEMO_URL, LS_DEMO_USERNAME, LS_DEMO_PASSWORD)
        lssession.expire_survey(self.surveyid)
        lssession.close()


    def createreport(self):
        '''Create the PDF report for the church'''

        return True
