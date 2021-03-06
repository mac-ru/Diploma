# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-06 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cdata',
            fields=[
                ('cd', models.CharField(default=b'', max_length=50, primary_key=b'True', serialize=False, unique=b'True')),
                ('code', models.CharField(default=b'', max_length=3)),
                ('date', models.CharField(default=b'', max_length=50)),
                ('confirmed', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('stringency_actual', models.CharField(default=b'', max_length=50, null=b'True')),
                ('stringency', models.CharField(default=b'', max_length=50, null=b'True')),
            ],
        ),
        migrations.CreateModel(
            name='cntr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=3)),
            ],
        ),
    ]
