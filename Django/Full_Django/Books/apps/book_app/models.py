from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=70)
	published_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	category = models.CharField(max_length=60)
	in_print = models.BooleanField()
