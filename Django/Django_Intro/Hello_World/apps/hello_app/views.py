from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	print 'hello world'
	return render(request, 'hello_app/index.html')