# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readers', '0008_reader_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='text_review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
