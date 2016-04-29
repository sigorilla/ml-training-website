# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

import datetime


class Link(models.Model):

    class Meta:
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'
        ordering = ['title']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    TARGET_CHOICES = (
        ('EM', ''),
        ('BL', '_blank'),
        ('SF', '_self'),
        ('PR', '_parent'),
        ('TP', '_top'),
    )

    title = models.CharField(max_length=200, verbose_name='текст')
    href = models.CharField(max_length=200, verbose_name='ссылка')
    target = models.CharField(max_length=2, choices=TARGET_CHOICES, default='EM', verbose_name='как открыть?')


class Event(models.Model):

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'pk': self.pk})

    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    active = models.BooleanField(default=False, verbose_name='активно')
    image = models.TextField(verbose_name='изображение', blank=True)
    links = models.ManyToManyField(Link, verbose_name='ссылки', blank=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'опубликовано недавно?'
