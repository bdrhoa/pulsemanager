# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-17 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='surveyid',
            field=models.IntegerField(default=0, verbose_name='Survey ID'),
        ),
    ]
