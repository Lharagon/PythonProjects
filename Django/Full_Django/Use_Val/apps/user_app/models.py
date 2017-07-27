from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse

# Create your models here.
class UserManager(models.Manager):
	def validator(self, user, request):
		if len(user) > 16:
			messages.error(request, "User name can't be more than 16 characters long")
			return "error1"
		if len(user) < 8:
			messages.error(request, "User name can't be less than 8 characters long")
			return "error2"

		print 'THIS IS THE USER ARGUMENT INSIDE OF THE MODEL', user
		entry = user
		return "pass"

class Username(models.Model):
	user_name = models.CharField(max_length=35)
	created_at = models.DateTimeField(auto_now_add=True)
	objects = UserManager()

