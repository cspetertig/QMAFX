# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Strategy(models.Model):
    STATUS_CHOICES=(
        ('INITIAL','INITIAL'),
        ('SAVED','SAVED'),
        ('PROCESSING','PROCESSING'),
        ('TESTED','TESTED')
    )
    user=models.ForeignKey(User)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500,blank=True)
    code=models.TextField()
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='INITIAL')
    def __str__(self):
        return self.title



