from django.contrib import admin
from .models import TelegramToSlack


@admin.register(TelegramToSlack)
class TelegramToSlack(admin.ModelAdmin):
    list_display = ('name', 'url', 'slack_hook', 'channel')
    search_fields = ('name', 'url', 'slack_hook', 'channel')
