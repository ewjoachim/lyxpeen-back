# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20170618_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singer',
            old_name='active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='songfile',
            old_name='active',
            new_name='is_active',
        ),
    ]
