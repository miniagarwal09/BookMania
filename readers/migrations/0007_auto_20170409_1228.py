# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0006_auto_20170409_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_logo',
            field=models.ImageField(default='no_image.png', upload_to=b''),
        ),
    ]
