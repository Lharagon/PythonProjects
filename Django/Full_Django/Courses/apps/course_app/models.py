from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=70)
	created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	course_id = models.ForeignKey(Course)
	user_name = models.CharField(max_length=50)
	comment = models.TextField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)