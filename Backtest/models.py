# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Strategy.models import Strategy
# Create your models here.

class BackTest(models.Model):
    STATUS_CHOICES=(
        ('DONE','DONE'),
        ('PROCESSING','PROCESSING'),
        ('ERROR','ERROR')
    )
    strategy = models.ForeignKey(Strategy)
    Profit=models.CharField(max_length=100,null=True)
    MaxDrawdown = models.CharField(max_length=100, null=True)
    Sharp = models.CharField(max_length=100, null=True)
    Profitfactor = models.CharField(max_length=100, null=True)
    Winrate = models.CharField(max_length=100, null=True)
    Std = models.CharField(max_length=100, null=True)
    Mean = models.CharField(max_length=100, null=True)
    Buynumber = models.CharField(max_length=100, null=True)
    Buyprofit = models.CharField(max_length=100, null=True)
    Sellnumber = models.CharField(max_length=100, null=True)
    Sellprofit = models.CharField(max_length=100, null=True)
    task=models.CharField(max_length=100,null=True)
    error_info=models.TextField(max_length=1000,null=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=50,default='PROCESSING')