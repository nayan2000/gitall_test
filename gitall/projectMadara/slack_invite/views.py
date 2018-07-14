from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponseRedirect

from .forms import InviteForm
from .config import *

def home(request):
	if request.method == 'POST':
		form = InviteForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			
			url = 'https://' + config.SLACK_URL + '/api/users.admin.invite'
			form = {
				'email' : email,
				'token' : config.SLACK_TOKEN,
				'set_active' : 'true',
			}
			# sending thr request to slack
			r = requests.post(url, data=form)

			return HttpResponseRedirect('/join/thanks')
	else:
		form = InviteForm()
		community = config.SLACK_TEAM

	context = {
		'form': form,
		'community': community,
	}
	
	return render(request, 'slack_invite/home.html', context)

# why this again?
def home_files (request, filename):
	return render(request, filename, {}, content_type='text/plain')

def thanks(request):
	community = config.SLACK_TEAM
	context = {
		'community': community,
	}
	return render(request, "slack_invite/thanks.html", )