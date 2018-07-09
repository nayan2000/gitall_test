from django.shortcuts import render, redirect
from .forms import TagForm
from django.contrib import messages
from accounts.models import UserAccount
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404

def create_tag(request):
	"""
		This makes sure that the form accpets a POST requests (of some data) or Nothing.
		Without this the form would even accept empty totos.
	"""
	if not request.user.is_authenticated():
		raise Http404

	form = TagForm(request.POST or None)
	flag = 0
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Tag created!")
		return redirect("toto:write")
	message = "Spaces are not allowed in tag name."
	messages.error(request, message, extra_tags="")
	context = {
		'title': "Create",
		'form' : form,
	}
	return render(request, 'tags/add.html', context)
