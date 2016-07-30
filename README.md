# Slack Telegram Bot
===================

+ Set `SECRET_KEY` in settings.py
+ Build docker: docker build -t slack-telegram-bot ./
+ Run docker: docker run -d -p 0.0.0.0:8035:8035 --name slack-telegram-bot --restart=always slack-telegram-bot
+ Setup hooks in the admin interface
+ Visit admin at http://localhost:8035/admin with (Username=admin, Password=admin by default)
