from django.db import models


class SlackToTelegram(models.Model):
    name = models.CharField(null=False, verbose_name='Name', max_length=128,
                            help_text='A short description for this forwarding.')

    url = models.CharField(null=False, verbose_name='Url', max_length=128, db_index=True,
                           help_text='If you set this to x, you should set slack webhook '
                                     'to https://my_address/slack/x/')

    bot_token = models.CharField(null=False, verbose_name='Bot Token', max_length=128,
                                 help_text='The token of the bot you want to send telegram '
                                           'messages from.')

    chat_id = models.CharField(null=False, verbose_name='Chat ID', max_length=128,
                               help_text='The chat id you want to send the telegram message to. This could be '
                                         'either user id, group id, or channel username (Starting with @)')

    def __str__(self):
        return self.name
