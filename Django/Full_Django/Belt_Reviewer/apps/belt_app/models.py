# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import re
from django.contrib import messages
from django.db.models import Count, Avg
import bcrypt

name_re = re.compile(r'^[A-Za-z\s]{1,}$')
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_re = re.compile(r'^[a-zA-Z0-9.+_-]{8,}.\*?$')
# Create your models here.
class UserManager(models.Manager):
	def Reg_validator(self, post_data, request):
		errors = []
		empty = False

		print "IT WENT INTO VALIDATION"
		if len(post_data['full_name']) == 0:
			empty = True
		elif not name_re.match(post_data['full_name']):
			errors.append("First name can't be fewer than 2 characters")

		if len(post_data['alias']) == 0:
			empty = True
		elif not name_re.match(post_data['alias']):
			errors.append("Alias can't be fewer than 2 characters")

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
			hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), user.password.encode())
			
			if  hashed_pass == user.password:
				print "USER INFO AFTER SIGNING ON", user.full_name
				# request.session['user'] = user.first_name
				return True
			messages.error(request, "Not valid username or password")
			return False
		except:
			messages.error(request, "Not valid username or password")
			return False
		
class User(models.Model):
	full_name = models.CharField(max_length=100)
	alias = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class Author(models.Model):
	name = models.CharField(max_length=70)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, related_name="my_books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
	content = models.TextField()
	reviewer = models.ForeignKey(User, related_name='books_reviewed')
	book_reviewed = models.ForeignKey(Book, related_name='reviews')
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def stars(self):
		star_rating = ""
		for num in range(1,6):
			if num <= self.rating:
				star_rating += '★'
			else:
				star_rating += 	"☆"
		return star_rating




# class User
