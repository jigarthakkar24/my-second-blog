# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-09 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20161009_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
    ]
