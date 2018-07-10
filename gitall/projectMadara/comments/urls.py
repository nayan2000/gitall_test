from django.conf.urls import url
from django.contrib import admin

app_name = 'comments'

from .views import (
    comment_thread,
    comment_delete

    )

urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),
     url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]