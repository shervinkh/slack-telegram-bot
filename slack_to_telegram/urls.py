from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<notification_url>.*)/$', views.slack_notification, name='slack_notification'),
]