from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
import re
from django.contrib import messages
from django.db.models import Count
import bcrypt

name_re = re.compile(r'^[A-Za-z]{1,}$')
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_re = re.compile(r'^[a-zA-Z0-9.+_-]{8,}.\*?$')
# Create your models here.
class UserManager(models.Manager):
	def Reg_validator(self, post_data, request):
		errors = []
		empty = False

		print "IT WENT INTO VALIDATION"
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
	password = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Secret(models.Model):
	secret = models.CharField(max_length=120)
	creator = models.ForeignKey(User, related_name="my_posts")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	likes = models.ManyToManyField(User, related_name="liked_secret")

	def elapsed_time (self):
		timezone = self.created_at.tzinfo
		timediff = datetime.datetime.now(timezone).replace(microsecond=0, second=0) - self.created_at.replace(microsecond=0)
		timediff = timediff
		return timediff

	def total_likes(self):
		total = self.likes.count()
		print "These are the total likes for this post", total
		return total

	# def has_liked(self):
	# 	try:
	# 		liked_by = self.likes.get(id=request.session['user_id'])
	# 		print "this worked I think"
	# 		return True
	# 	except:
	# 		print "did not work", self.likes.filter(id=1)
	# 		return False



