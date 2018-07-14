from django.conf.urls import url

from .views import home, thanks

urlpatterns = [
    url('^$', home, name='invite_home'),
    url('^thanks/$', thanks, name='thanks'),
]