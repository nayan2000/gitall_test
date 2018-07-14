# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Toto

# Register your models here.
class TotoAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'timestamp',]
	class Meta:
		model = Toto
		fields = ('title')
		

admin.site.register(Toto, TotoAdmin)