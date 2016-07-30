from django.db import models


class TelegramToSlack(models.Model):
    name = models.CharField(null=False, verbose_name='Name', max_length=128,
                            help_text='A short description for this forwarding.')

    url = models.CharField(null=False, verbose_name='Url', max_length=128, db_index=True,
                           help_text='If you set this to x, you should set telegram webhook '
                                     'to https://my_address/telegram/x/')

    chat_id = models.CharField(null=False, verbose_name='Chat ID', max_length=128,
                               help_text='The telegram chat id you want to listen to. This could be '
                                         'either user id, group id, or channel username (Starting with @)')

    slack_hook = models.CharField(null=False, verbose_name='Slack Hook', max_length=512,
                                  help_text='The url of the slack webhook you created')

    channel = models.CharField(null=True, blank=True, verbose_name='Channel', max_length=128,
                               help_text='The channel or user you want to send the slack message to. '
                                         'Channels start with # and users start with @.')

    def __str__(self):
        return self.name
