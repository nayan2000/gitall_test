# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.conf import settings
# sending emails
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm

# Create your views here.
def contact(request):
	title = "Contact"
	if request.method == "POST":
		form = ContactForm(request.POST or None)
		confirm_message = None

		if form.is_valid(): 
			name = form.cleaned_data['name']
			message = form.cleaned_data['message']
			mail_id = form.cleaned_data['email']
			mail_subject = "Contact | GitAll"
			mail_message = "%s with email id [%s] sent the following message: <br/> %s" %(name, mail_id , message)
			mail_from = 'accounts@gitall.tech'
			mail_to = ['team@gitall.tech']
			
			send_mail(
					mail_subject, mail_message, 
					mail_from, mail_to,
		    		fail_silently=False,
					)
			title = "Thanks!"
			confirm_message = "Thanks for the message. We'll get right back to you!"
			form = None

		# Initially the form is visible; so no confirm message needed, hence None
		# After the form has been filled, there's a message but no form. 
		context = {
				"title" : title,
				"confirm_message" : confirm_message,
				"form" : form,
			}
	else:
		form = ContactForm()
		context = {
			"form": form
		}


	template = 'main/contact.html'
	return render(request, template, context)