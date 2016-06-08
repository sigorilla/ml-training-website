# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-08 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0010_auto_20160525_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'analysis', 'verbose_name_plural': 'analyses'},
        ),
        migrations.AddField(
            model_name='material',
            name='code',
            field=models.URLField(blank=True, verbose_name='code link'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.URLField(verbose_name='url for logo'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='link',
            field=models.URLField(verbose_name='site link'),
        ),
    ]