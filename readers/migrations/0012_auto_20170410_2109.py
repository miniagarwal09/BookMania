# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0011_auto_20170410_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='dob',
            field=models.DateField(auto_now=True),
        ),
    ]
