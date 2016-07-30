from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<notification_url>.*)/$', views.telegram_notification, name='telegram_notification'),
]