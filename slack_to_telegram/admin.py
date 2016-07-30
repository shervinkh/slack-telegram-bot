from django.contrib import admin
from .models import SlackToTelegram


@admin.register(SlackToTelegram)
class SlackToTelegramAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'bot_token', 'chat_id')
    search_fields = ('name', 'url', 'bot_token', 'chat_id')
