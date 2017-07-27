# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-22 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=70)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=60)),
            ],
        ),
    ]
