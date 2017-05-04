# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Publisher(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    publisher_name = models.CharField(max_length=50)
    publication_name = models.CharField(max_length=50)
    joined_on = models.DateField(auto_now=True)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.publisher_name+" of "+self.publication_name



