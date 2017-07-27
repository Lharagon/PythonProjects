from __future__ import unicode_literals
from django.db import models
import re
from django.contrib import messages
from datetime import datetime, timedelta

name_re = re.compile(r'^[A-Za-z]{1,}$')
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_re = re.compile(r'^[a-zA-Z0-9.+_-]{8,}.\*?$')
# Create your models here.
class UserManager(models.Manager):
	def Reg_validator(self, post_data, request):
		errors = []
		empty = False

		# print post_data['birthday'] - timedelta(months=216)

		if len(post_data['first_name']) == 0:
			empty = True
		elif not name_re.match(post_data['first_name']):
			errors.append("First name can't be fewer than 2 characters")

		if len(post_data['last_name']) == 0:
			empty = True
		elif not name_re.match(post_data['last_name']):
			errors.append("Last name can't be fewer than 2 characters")

		if len(post_data['email']) == 0:
			empty = True
		elif not email_re.match(post_data['email']):
			errors.append("Enter valid email")
		else:
			user = User.objects.filter(email = post_data['email'])
			if len(user) > 0:
				errors.append('Email already taken')

		if len(post_data['birthday']) == 0:
			empty = True

		if len(post_data['password']) == 0:
			empty = True
		elif not password_re.match(post_data['password']):
			errors.append("Password must be more than 8 characters.")

		if post_data['password'] != post_data['passconf']:
			errors.append("Passwords don't match")

		if empty:
			errors.append("All fields are required")

		if len(errors) > 0:
			for error in errors:
				messages.error(request, error)

			return False
		
		return True
		
	def Log_validator(self, post_data, request):
		try:
			user = User.objects.get(email = post_data['email'])
			if post_data['password'] == user.password:
				print "USER INFO AFTER SIGNING ON", user.first_name
				# request.session['user'] = user.first_name
				return True
			messages.error(request, "Not valid username or password")
			return False
		except:
			messages.error(request, "Not valid username or password")
			return False
		

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	birthday = models.DateTimeField()
	password = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()