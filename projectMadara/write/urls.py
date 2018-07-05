from django.conf.urls import url

from . import views
urlpatterns = [
    url('^thelistthatyouexpected$', views.toto_list, name='list'),
    url('^write/$', views.toto_create, name='write'),
    url('^draft/$', views.toto_draft, name='draft'),
    url('^(?P<slug>[\w-]+)/$', views.toto_detail, name='detail'),
    url('^(?P<slug>[\w-]+)/edit/$', views.toto_edit, name='edit'),
    url('^(?P<slug>[\w-]+)/delete/$', views.toto_delete, name='delete'),
]
