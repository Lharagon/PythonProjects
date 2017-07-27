from django.shortcuts import render, HttpResponse
import datetime


top = datetime.datetime.now().strftime('%b %d, %Y')
bottom = datetime.datetime.now().strftime('%I:%M %p')
alls = datetime.datetime.now().strftime('%c')
# Create your views here.
def index(request):
	context = {
		"date": str(top),
		"time": str(bottom) 
	}
	return render(request, 'time_app/index.html',context)