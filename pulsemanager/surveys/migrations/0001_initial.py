# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-17 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyname', models.CharField(blank=True, max_length=255, verbose_name='Name of Survey')),
            ],
        ),
    ]
