# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# phone number of the user
from phonenumber_field.modelfields import PhoneNumberField

# validators
from django.core.validators import URLValidator

# uploading profile photos
def upload_location(instance, filename):
	return "account_photos/%s/%s" %(instance.user, filename)

# Create your models here.
class UserAccount(models.Model):
	user 			= models.OneToOneField(User)
	photo		 	= models.ImageField(
						upload_to=upload_location, # there needs to be a upload location tho
						# most probably a cdn server
						blank=True,
						null=True, 
						width_field="width_field",
						height_field="height_field")
	width_field 	= models.IntegerField(default=0, null=True)
	height_field 	= models.IntegerField(default=0, null=True)
	bio  			= models.TextField(max_length=60, null=True, blank=True, verbose_name="You in 60 words.")
	phone 			= PhoneNumberField(blank=True, verbose_name="Contact Number")
	status 			= models.CharField(max_length=128, default="Student")
	totos 			= models.IntegerField(default=0, verbose_name="Contribution")
	user_since 		= models.DateTimeField(auto_now=True)

	# social links
	email			= models.EmailField(verbose_name="email address", 
										max_length=255,
										unique=True,
										null=True, blank=True)
	custom_link		= models.URLField(null=True, blank=True)
	facebook_link	= models.URLField(null=True, blank=True)
	twitter_link 	= models.URLField(null=True, blank=True)
	linkedin_link	= models.URLField(null=True, blank=True)
	github_link 	= models.URLField(null=True, blank=True)
	reddit_link		= models.URLField(null=True, blank=True)



	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return self.reverse("accounts:public_user_account", kwargs={"username":self.user__username})

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User) # User is coming from the user=models.OneToOneField(<User>)
def create_account(sender, instance, created, *args, **kwargs):
	if created:
		account, new = UserAccount.objects.get_or_create(user=instance)

post_save.connect(create_account, sender=settings.AUTH_USER_MODEL)