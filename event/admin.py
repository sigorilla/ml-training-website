from django.contrib import admin
from models import Event


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Create new post', {'fields': ['title', 'content', 'active']})
    ]
    list_display = ('title', 'pub_date', 'active', 'was_published_recently')
    list_filter = ['pub_date', 'active']
    search_fields = ['title', 'content']
    readonly_fields = ('pub_date',)

admin.site.register(Event, EventAdmin)
