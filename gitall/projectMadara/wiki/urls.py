from django.conf.urls import url
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', wiki_home, name='wiki_home'),
    url('^wiki_add/$', wiki_add, name='wiki_add'),
    url('^(?P<slug>[\w-]+)/(?P<text>[\w-]+)/delete_tag/$', delete_tag, name='delete_tag'),
    url('^(?P<slug>[\w-]+)/add_tag/$', add_tag, name='add_tag'),
    # url('^wiki_details/(\d+)/$', wiki_details, name='wiki_details'),
    url('^(?P<slug>[\w-]+)/$', wiki_details, name='wiki_details'),
    url('^(?P<slug>[\w-]+)/edit/$', wiki_edit, name='wiki_edit'),
    # url('^wiki_edit/(\d+)/$', wiki_edit, name='wiki_edit'),
    # url('^wiki_comment/(\d+)/$', wiki_comment, name='wiki_comment'),
    url('^(?P<slug>[\w-]+)/wiki_community/$', wiki_community, name='wiki_community'),
    url('^(?P<slug>[\w-]+)/wiki_resource/$', wiki_resource, name='wiki_resource'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
