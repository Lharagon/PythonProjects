from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Username

# Create your views here.
def index(request):
	return render(request, 'user_app/index.html')

def success(request):
	usernames = Username.objects.all()

	context = {
		"user_list": usernames
	}
	return render(request, 'user_app/success.html', context)

def process(request):
	new_user = request.POST['username']
	print "THIS IS THE USER NAME I INPUTED", new_user
	user = Username.objects.validator(new_user, request)
	print user
	if user == 'error1':
		return redirect('/')
	elif user == 'error2':
		return redirect('/')

	user = Username.objects.create(user_name = new_user)
	messages.success(request, "Thank you {} for signing up".format(new_user))


	return redirect ('/success')



