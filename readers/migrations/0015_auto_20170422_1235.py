# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0014_auto_20170422_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_review',
            name='review',
            field=models.TextField(max_length=200),
        ),
    ]
