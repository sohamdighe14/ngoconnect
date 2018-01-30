# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 15:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('occupation', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
    ]
