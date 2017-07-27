from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Client(models.Model):
	business_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	client_notes = models.TextField(default='None')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
	project_name = models.CharField(max_length=255)
	project_notes = models.TextField(default='None')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	belongs_to = models.ForeignKey(Client, related_name = "projects")

