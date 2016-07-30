import requests


def escape_markdown(str):
    str = str.replace('*', '\\*')
    str = str.replace('_', '\\_')
    str = str.replace('[', '\\[')
    return str


def get_chat_id(message_json):
    if 'chat' in message_json:
        return message_json['chat']['id']
    elif 'from' in message_json:
        return message_json['from']['id']
    else:
        return None


def get_sender_name(message_json):
    name = None

    if 'from' in message_json and 'first_name' in message_json['from']:
        name = message_json['from']['first_name'] or ''
        if 'last_name' in message_json['from']:
            name += ' ' + (message_json['from']['last_name'] or '')

    return name


class TelegramBot(object):
    def __init__(self, token):
        self.token = token

    def call_remote_method(self, method, parameters):
        url = 'https://api.telegram.org/bot{token}/{method}'.format(token=self.token,
                                                                    method=method)
        return requests.post(url, json=parameters)

    def send_message(self, id, text):
        parameters = {'chat_id': id, 'text': text, 'parse_mode': 'Markdown',
                      'disable_web_page_preview': True}
        return self.call_remote_method('sendMessage', parameters)


class SlackBot(object):
    def __init__(self, url):
        self.url = url

    def send_message(self, text, username=None, channel=None):
        data = {'text': text}

        if username:
            data['username'] = username

        if channel:
            data['channel'] = channel

        return requests.post(self.url, json=data)
