from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

import datetime

DEFAULT_IMAGE = '/static/img/competition-logo.svg'


class Link(models.Model):

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
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

    title = models.CharField(max_length=200, verbose_name=_('title'))
    href = models.CharField(max_length=200, verbose_name=_('href'))
    target = models.CharField(max_length=2, choices=TARGET_CHOICES, default='EM', verbose_name=_('target'))


class Competition(models.Model):

    class Meta:
        verbose_name = _('competition')
        verbose_name_plural = _('competitions')
        ordering = ['finish_date']

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('competition:detail', kwargs={'pk': self.pk})

    def get_image_url(self):
        return self.image if not self.image == DEFAULT_IMAGE else None

    @property
    def is_finished(self):
        now = timezone.now()
        return now > self.finish_date

    title = models.CharField(max_length=200, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('description'))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_('published date'))
    upd_date = models.DateTimeField(auto_now=True, verbose_name=_('updated date'), blank=True)
    start_date = models.DateTimeField(verbose_name=_('start date'), default=timezone.now, blank=False)
    submission_deadline = models.DateTimeField(default=timezone.now, verbose_name=_('submission deadline'))
    entry_deadline = models.DateTimeField(default=timezone.now, verbose_name=_('entry deadline'))
    finish_date = models.DateTimeField(verbose_name=_('finish date'), default=timezone.now, blank=False)
    active = models.BooleanField(default=True, verbose_name=_('active?'))
    image = models.URLField(verbose_name=_('url for logo'), default=DEFAULT_IMAGE)
    link = models.URLField(verbose_name=_('site link'), default='#', blank=False)
    links = models.ManyToManyField(Link, verbose_name=_('links'), blank=True)
    author = models.ForeignKey(User, verbose_name=_('author'), default=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('was published recently?')


class Material(models.Model):

    class Meta:
        verbose_name = _('material')
        verbose_name_plural = _('materials')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=200, verbose_name=_('title'))
    article = models.URLField(verbose_name=_('article link'), blank=True)
    video = models.URLField(verbose_name=_('video link'), blank=True)
    slides = models.FileField(verbose_name=_('slides'), blank=True, upload_to='slides')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
