FROM    ubuntu:trusty
RUN     apt-get -y update

# Install required packages
RUN     apt-get -y install python-pip nginx
RUN     pip install django==1.8.14 gunicorn==19.6.0 supervisor==3.2.3 requests==2.10.0

# Add SlackTelegramBot to /app
ADD     . /app/SlackTelegramBot/
RUN     cd /app/SlackTelegramBot/ && python manage.py migrate
RUN     cd /app/SlackTelegramBot/ && echo yes | python manage.py collectstatic
RUN     cd /app/SlackTelegramBot/ && python manage.py initialize_admin

# Link supervisor configs
RUN     cp /app/SlackTelegramBot/conf/supervisor/supervisord.conf /etc/supervisord.conf
RUN     ln -s /app/SlackTelegramBot/conf/supervisor/programs /etc/supervisor
RUN     ln -s /app/SlackTelegramBot/conf/nginx/sites/slack-telegram-bot /etc/nginx/sites-enabled/
RUN     rm /etc/nginx/sites-enabled/default

# Web Interface
EXPOSE  :8035

CMD     ["/usr/local/bin/supervisord"]
