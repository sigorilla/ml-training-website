# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0009_auto_20160525_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.URLField(default='/static/img/competition-logo.svg', verbose_name='url for logo'),
        ),
    ]