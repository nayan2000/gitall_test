"""
     it is to display the models in django admin pannel.
"""

from django.contrib import admin

# Register your models here.
from .models import Comment

# comment model is registered here
admin.site.register(Comment)
