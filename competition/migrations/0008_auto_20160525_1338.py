# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0007_auto_20160525_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='article',
            field=models.URLField(blank=True, verbose_name='article link'),
        ),
        migrations.AlterField(
            model_name='material',
            name='slides',
            field=models.URLField(blank=True, verbose_name='slides link'),
        ),
        migrations.AlterField(
            model_name='material',
            name='video',
            field=models.URLField(blank=True, verbose_name='video link'),
        ),
    ]