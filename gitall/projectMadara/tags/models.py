from django.db import models
from django.contrib.auth.models import User
from write.models import *
# from django.template.defaultfilters import slugify

class Tag(models.Model):
    text = models.CharField(max_length = 30, unique=True)
    added_by = models.ForeignKey(User, default='0')
    def __str__(self):
        return self.text
