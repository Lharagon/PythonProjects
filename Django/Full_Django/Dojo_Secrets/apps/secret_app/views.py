from django.shortcuts import render, redirect, HttpResponse
from .models import User, Secret
from django.contrib import messages
from django.db.models import Count
import json

def index(request):
	if 'user' in request.session:
		return redirect('/success')
	return render(request, 'secret_app/index.html')

def success(request):
	# if request.method == 'POST':
	secrets = Secret.objects.all().order_by("-created_at")[:5]
	this_user = User.objects.get(id=request.session['user_id'])
	context = {
		"secret_list" : secrets,
		"this_user": this_user
		}

	return HttpResponse(json.dumps(secrets))
	# messages.success(request, "Sign in First Please")
	# return redirect('/')

def login(request):
	if request.method == 'POST':
		validated = User.objects.Log_validator(request.POST, request)
	
		if validated:
			user = User.objects.get(email=request.POST['email'])
			request.session['user'] = user.first_name
			request.session['user_id'] = user.id
			return redirect('/success')
	
		return redirect('/')

	return redirect('/')

def register(request):
	if request.method == 'POST':
		validated = User.objects.Reg_validator(request.POST, request)
		if validated:
			user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password =request.POST['password'])
			request.session['user'] = user.first_name
			request.session['user_id'] = user.id
			return redirect('/success')

		return redirect('/')

	return redirect('/')

def log_out(request):
	if request.method == 'POST':
		request.session.clear();
		messages.success(request, "Hurry Back!!!!")
		return redirect('/')

def post(request):
	if request.method == 'POST':
		poster = User.objects.get(id=request.session['user_id'])
		secrete = Secret.objects.create(secret = request.POST['secret'], creator = poster)
		print "This is the user name of current user", request.session['user']
		print "This is the user id of current user", request.session['user_id']
		return redirect('/success')
		
def like(request,sid, uid):
	# try:
	# 	existing_like:
	liked_see = Secret.objects.get(id = sid)
	liking_use = User.objects.get(id = uid)
	liked_see.likes.add(liking_use)

	return redirect('/success')

def delete(request, id):
	Secret.objects.get(id = id).delete()

	return redirect('/success')

def popular(request):

	secrets = Secret.objects.annotate(tots=Count('likes')).order_by('-tots') [:5]
	this_user = User.objects.get(id=request.session['user_id'])

	context = {
		'secret_list': secrets,
		"this_user": this_user 
	}

	return render(request, 'secret_app/popular.html', context)
