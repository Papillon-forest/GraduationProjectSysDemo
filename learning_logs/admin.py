from django.contrib import admin

# Register your models here.
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ['text', 'owner', 'date_added']

    list_filter = ['text', 'owner']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['text', 'topic', 'key_days', 'key_days_middle', 'key_days_end', 'user_retention', 'date_added']
    list_filter = ['text', 'topic', 'key_days', 'key_days_middle', 'key_days_end']
    search_fields = ['text']
    list_per_page = 10


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
