from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest

from bot_utils.bot import TelegramBot, escape_markdown
from .models import SlackToTelegram

@csrf_exempt
def slack_notification(request, notification_url):
    if request.method != 'POST':
        return HttpResponseForbidden()
    try:
        channel_name = escape_markdown(request.POST['channel_name'])
        user_name = escape_markdown(request.POST['user_name'])
        user_id = request.POST['user_id']
        text = escape_markdown(request.POST['text'])

        if user_id != 'USLACKBOT':
            message = u'*{user}* _in_ #{channel}:\n{text}'

            message = message.format(user=user_name, channel=channel_name, text=text)

            forward_list = SlackToTelegram.objects.filter(url=notification_url).values_list('bot_token', 'chat_id')
            for (bot_token, chat_id) in forward_list:
                TelegramBot(bot_token).send_message(chat_id, message)

        return HttpResponse(status=200)
    except Exception:
       return HttpResponseBadRequest()
