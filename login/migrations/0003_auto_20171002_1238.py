# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-02 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20171002_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='gihtub_repo',
            new_name='github_repo',
        ),
    ]
