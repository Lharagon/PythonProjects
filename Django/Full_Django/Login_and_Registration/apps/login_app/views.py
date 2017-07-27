from django.shortcuts import render, redirect
from .models import User

def index(request):
	return render(request, 'login_app/index.html')

def success(request):
	return render(request, 'login_app/success.html')

def login(request):
	post_data = request.POST
	validated = User.objects.Log_validator(post_data, request)
	
	if validated:
		user = User.objects.get(email = post_data['email'])
		request.session['user'] = user.first_name
		return redirect('/success')
		
	return redirect('/')

def register(request):
	post_data = request.POST
	
	validated = User.objects.Reg_validator(post_data, request)
	if validated:
		user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], birthday = request.POST['birthday'], password =request.POST['password'])
		request.session['user'] = user.first_name
		return redirect('/success')

	return redirect('/')
