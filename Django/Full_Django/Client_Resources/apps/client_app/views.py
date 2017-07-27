from django.shortcuts import render, redirect
from .models import Client, Project
from django.contrib import messages
import re
# Create your views here.

phone_re = re.compile(r'^([1-9]\d{2}-\d{3}-\d{4})$')
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	client_list = Client.objects.all()
	context = {
		'client_list': client_list
	}
	return render(request, 'client_app/index.html', context)

def add_p(request, id):
	project_client = Client.objects.get(id = id)
	context = {
		'proj_client': project_client
	}
	return render(request, 'client_app/add_project.html', context)

def adding_clie(request):
	if request.method == 'POST':
		data = request.POST
		cool = True

		if not data['business']:
			messages.error(request, "Field can't be blank")
			cool = False

		if not email_re.match(data['email']):
			messages.error(request,"Enter valid email")
			cool = False

		if not phone_re.match(data['phone']):
			messages.error(request,"Enter proper phone number")
			cool = False

		if not cool:
			return redirect('client/add')
		else:
			new_client = Client.objects.create(business_name=data['business'], email = data['email'], phone = data['phone'], client_notes = data['notes'])
			return redirect('client/%s' % new_client.id)



def add_c(request):
	return render(request, 'client_app/add_client.html')

def client_pro(request, id):
	client = Client.objects.get(id = id)
	project_list = Project.objects.filter(belongs_to = client)

	context = {
		'client': client,
		'project_list': project_list
	}
	return render(request, 'client_app/client.html', context)

def project_pro(request, id):
	project = Project.objects.get(id = id)
	context = {
		'proj': project
	}
	return render(request, 'client_app/project.html', context)

def adding_proj(request, id):
	if request.method == 'POST':
		data = request.POST
		cool = True

		if not data['project_name']:
			messages.error(request, "Project can't be blank")
			cool = False

		if not cool:
			return redirect('/adding_proj/%s' % (id))

		client = Client.objects.get(id = id)
		new_project = Project.objects.create(project_name = data['project_name'], project_notes = data['notes'], belongs_to = client)

		return redirect('/projects/%s' % (new_project.id))
