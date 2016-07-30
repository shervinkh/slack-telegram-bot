from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest

from bot_utils.bot import SlackBot, get_chat_id, get_sender_name
from .models import TelegramToSlack

import json


@csrf_exempt
def telegram_notification(request, notification_url):
    if request.method != 'POST':
        return HttpResponseForbidden()
    try:
        notification = json.loads(request.body)

        if 'message' in notification:
            message = notification['message']

            if ('text' in message) or ('caption' in message):
                text = message.get('text', '') + message.get('caption', '')
                chat_id = get_chat_id(message)
                name = get_sender_name(message)
                if chat_id:
                    forward_list = TelegramToSlack.objects.filter(url=notification_url, chat_id=chat_id)\
                        .values_list('slack_hook', 'channel')
                    for (hook, channel) in forward_list:
                        SlackBot(hook).send_message(text, name, channel)

        return HttpResponse(status=200)
    except Exception:
        return HttpResponseBadRequest()
