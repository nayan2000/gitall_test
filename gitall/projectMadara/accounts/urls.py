from django.conf.urls import url
from .views import *

urlpatterns = [
	# for updating
	url(r'^update/$', update_user_account, name="update_user_account"),
	# for outside world
	url(r'^(?P<username>[\w.@+-]+)/$', user_account, name="public_user_account"),
	# for the user himself 
	url(r'^$', self_user_account, name="self_user_account"),
]