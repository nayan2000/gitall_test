from django.conf.urls import url
from tags import views as tag_views
from . import views
urlpatterns = [
    url('^thelistthatyouexpected$', views.toto_list, name='list'),
    url('^write/$', views.toto_create, name='write'),
    url('^(?P<slug>[\w-]+)/(?P<text>[\w-]+)/delete_tag/$', views.delete_tag, name='delete_tag'),
    url('^(?P<slug>[\w-]+)/add_tag/$', views.add_tag, name='add_tag'),
    url('^draft/$', views.toto_draft, name='draft'),
    url('^(?P<slug>[\w-]+)/$', views.toto_detail, name='detail'),
    url('^(?P<slug>[\w-]+)/edit/$', views.toto_edit, name='edit'),
    url('^(?P<slug>[\w-]+)/delete/$', views.toto_delete, name='delete'),
]
