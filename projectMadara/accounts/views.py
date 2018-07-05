# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from .models import UserAccount
from .forms import UserAccountForm

# public user profile
def user_account(request, username):
	instance = get_object_or_404(UserAccount, user__username=username)
	context = {
	'instance'	: instance,
	'title'		: "User Account",		
	}
	template = "user_accounts/public_account.html"
	return render(request, template, context)

# private user profile.
@login_required
def self_user_account(request):
	instance = get_object_or_404(UserAccount, user=request.user)
	if not request.user.is_authenticated:
		raise Http404
	elif not request.user == instance.user:
		raise Http404

	context = {
		'instance'	: instance,
		'title'		: 'Your Account',
	}	

	template = "user_accounts/self_account.html"
	return render(request, template, context)

# ability to update the user profile
@login_required
def update_user_account(request):
	if not request.user.is_authenticated:
		raise Http404

	instance = get_object_or_404(UserAccount, user=request.user)

	if request.method == 'POST':
		form = UserAccountForm(request.POST or None, request.FILES or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Account Updated.")
			return HttpResponseRedirect("/u/")
		else:
			messages.error(request, "Something went wrong. Profile not created.")
	else:
		form = UserAccountForm(instance=instance)

	context = {
		'title': 'Update Your Account',
		'form' : form,
	}
	template = "user_accounts/update.html"
	return render(request, template, context)