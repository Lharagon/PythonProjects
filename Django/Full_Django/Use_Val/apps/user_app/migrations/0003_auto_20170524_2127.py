# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 21:27
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20170524_2035'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='username',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]