# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Event, Link


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Создать новое событие', {'fields': ['title', 'content', 'active']}),
        (u'Больше информации', {'fields': ['image', 'links'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'active', 'was_published_recently')
    list_filter = ['pub_date', 'active']
    search_fields = ['title', 'content']
    readonly_fields = ('pub_date',)

admin.site.register(Event, EventAdmin)
admin.site.register(Link)
