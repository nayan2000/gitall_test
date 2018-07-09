"""projectMadara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from django.contrib import admin

#
# To import urls for static files.
from django.conf import settings
from django.conf.urls.static import static

"""
Customizing the path location of the error pages [templates/errors/].
Django looks them up by default at templates/

"""
from django.conf.urls import handler404, handler500, handler400, handler403
from main import views as main_views
from tags import views as tag_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tags/', include('tags.urls', namespace="tags")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('main.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^u/', include('accounts.urls', namespace="accounts")),
    url(r'^join/', include('slack_invite.urls')),
    url(r'^tutorial/', include('write.urls', namespace="toto")),
    url(r'^comments/', include("comments.urls", namespace='comments')),
]

# When the debug mode is false,
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Defining the new error handlers
handler400 = main_views.error400
handler403 = main_views.error403
handler404 = main_views.error404
handler500 = main_views.error500
