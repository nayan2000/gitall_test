# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
	list_display = ['__str__',]
	class Meta:
		model = UserAccount
		fields = ['user']

admin.site.register(UserAccount, UserAccountAdmin)
