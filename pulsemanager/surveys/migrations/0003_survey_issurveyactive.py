# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-21 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_surveyid'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='issurveyactive',
            field=models.BooleanField(default=True, verbose_name='Is Survey Active'),
        ),
    ]
