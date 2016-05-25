from django.contrib import admin
from django.utils.translation import ugettext as _
from models import Competition, Material


class CompetitionAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Create new competition'), {'fields': [
            'title', 'content', 'link',
            'start_date', 'finish_date', 'entry_deadline', 'submission_deadline',
            'image', 'materials', 'active',
        ]})
    ]
    list_display = ('title', 'start_date', 'active', 'was_published_recently')
    list_filter = ['pub_date', 'upd_date', 'active']
    search_fields = ['title', 'content']
    readonly_fields = ('pub_date', 'upd_date',)

admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Material)
