# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Competition, Link


class CompetitionAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Создать новое соревнование', {'fields': [
            'title', 'content', 'link', 'active',
            'start_date', 'finish_date', 'entry_deadline', 'submission_deadline',
            'image'
        ]}),
        (u'Больше информации', {'fields': ['links'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'active', 'was_published_recently')
    list_filter = ['pub_date', 'active']
    search_fields = ['title', 'content']
    readonly_fields = ('pub_date',)

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Link)
