from django.shortcuts import render, redirect
from .models import Course, Comment

# Create your views here.
def index(request):
	courses = Course.objects.all()
	print courses
	context = {
		"course_list" : courses
	}

	return render(request, 'course_app/index.html', context)

def add(request):
	name = request.POST['name']
	description = request.POST['description']

	Course.objects.create(name = name, description = description)

	return redirect('/')

def destroy(request, id):
	course = Course.objects.get(id = id)
	context = {
		'course': course
	}
	return render(request, 'course_app/destroy.html', context)

def removing(request):
	entry = request.POST['entry']
	Course.objects.get(id = entry).delete()
	return redirect('/')

def comments(request, id):
	course = Course.objects.get(id = id)
	context = {
		'course': course
	}
	return render(request, 'course_app/comments.html', context)

def post(request):
	ids = int(request.POST['entry'])
	course = Course.objects.get(id=ids)
	user_name = request.POST['name']
	comm = request.POST['comment']
	comment = Comment.objects.create(course_id = course, user_name = user_name, comment = comm)
	return redirect('/courses/comments/'+str(ids))
