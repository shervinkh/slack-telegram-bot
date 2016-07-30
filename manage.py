#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SlackTelegramBot.settings")

    if sys.argv[1] == 'initialize_admin':
        from django.contrib.auth.models import User
        if User.objects.count() == 0:
            User.objects.create_superuser(username='admin', email='slack@telegram-bot.org',
                                          password='admin')
            print("Created initial admin user: (Username=admin, Password=admin)")
    else:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
