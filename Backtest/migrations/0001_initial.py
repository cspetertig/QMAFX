# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-20 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Strategy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profit', models.CharField(max_length=100, null=True)),
                ('MaxDrawdown', models.CharField(max_length=100, null=True)),
                ('Sharp', models.CharField(max_length=100, null=True)),
                ('Profitfactor', models.CharField(max_length=100, null=True)),
                ('Winrate', models.CharField(max_length=100, null=True)),
                ('Std', models.CharField(max_length=100, null=True)),
                ('Mean', models.CharField(max_length=100, null=True)),
                ('Buynumber', models.CharField(max_length=100, null=True)),
                ('Buyprofit', models.CharField(max_length=100, null=True)),
                ('Sellnumber', models.CharField(max_length=100, null=True)),
                ('Sellprofit', models.CharField(max_length=100, null=True)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strategy.Strategy')),
            ],
        ),
    ]
