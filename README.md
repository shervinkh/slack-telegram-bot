# Slack Telegram Bot
===================

+ Set `SECRET_KEY` in settings.py
+ Build docker: docker build -t slack-telegram-bot ./
+ Run docker: docker run -i -p 0.0.0.0:8035:8035 slack-telegram-bot
+ Setup hooks in the admin interface
+ Visit admin at http://localhost:8035/admin with (Username=admin, Password=admin by default)
