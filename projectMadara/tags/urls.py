from django.conf.urls import url

from . import views
urlpatterns = [
    url('^create_tag/$', views.create_tag, name='create_tag'),
]
