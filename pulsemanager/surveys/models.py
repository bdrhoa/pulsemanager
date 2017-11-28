from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from pulsemanager.users import models as user_models

import random

class Survey(models.Model):

    surveyid        = models.IntegerField(_('Survey ID'), primary_key=True, default=0)
    surveyname      = models.CharField(_('Name of Survey'), blank=True, max_length=255)
    issurveyactive  = models.BooleanField(_('Is Survey Active'),default=True)
    user            = models.ForeignKey(user_models.User,related_name='surveys')

    def __str__(self):
        return self.surveyname

    def get_absolute_url(self):
        return reverse('survyes:detail', kwargs={'surveyname': self.surveyname})

    # Copy the base Limesurvey survey and return the new id and name.
    #just stubbed for now
    def copy_limesurvey(self):

        self.surveyid       = random.randint(1000, 9999)
        self.surveyname     = "new survey"
        self.issurveyactive = True


    def createreport(self):

        return True
