from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'real_p_app/index.html')

def testimonials(request):
	return render(request, 'real_p_app/testimonials.html')

def about(request):
	return render(request, 'real_p_app/about.html')

def projects(request):
	return render(request, 'real_p_app/projects.html')