# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-02 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='gihtub_repo',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='login',
            name='wifi_password_1',
            field=models.CharField(default='Not Alloted', max_length=250),
        ),
        migrations.AddField(
            model_name='login',
            name='wifi_password_2',
            field=models.CharField(default='Not Alloted', max_length=250),
        ),
        migrations.AddField(
            model_name='login',
            name='wifi_username_1',
            field=models.CharField(default='Not Alloted', max_length=250),
        ),
        migrations.AddField(
            model_name='login',
            name='wifi_username_2',
            field=models.CharField(default='Not Alloted', max_length=250),
        ),
    ]
