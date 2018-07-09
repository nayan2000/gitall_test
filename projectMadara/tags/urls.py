from django.conf.urls import url

from . import views
urlpatterns = [
    url('^add_tag/$', views.create_tag, name='create_tag'),
]
