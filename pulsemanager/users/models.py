from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig
from django.db.models.signals import pre_save
from model_utils import FieldTracker

#from pulsemanager.surveys import models as survey_models

@python_2_unicode_compatible
class User(AbstractUser):
    tracker = FieldTracker()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #survey          = models.ForeignKey(survey_models.Survey, null=True, blank=True)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    churchname = models.CharField(_('Name of Church'), blank=True, max_length=255)
    acitvesurvey = models.BooleanField(_('Is Survey Active'), default=True) #just for toggle switch in UI

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_survey(self):
        return self.surveys.all().order_by('-updated_at')[0]
