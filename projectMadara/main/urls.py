from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^explore/$', explore, name='explore'),
    url(r'^partners/$', partners, name='partners'),
    url(r'^google5715b52ab8f3659c', google_verification,
        name='google_verification'),
]
