from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'survey_app/index.html')

def result(request):
	return render(request, 'survey_app/result.html')

def process(request):

	if 'counter' not in request.session:
		request.session['counter'] = 1
	else:
		request.session['counter'] += 1

	request.session['context'] = {
		'name' : request.POST['name'],
		'location' : request.POST['location'],
		'language' : request.POST['language'],
		'comment' : request.POST['comment']
	}

	return redirect('/result')

def go_back(request):
	print "Before", request.session['context']
	request.session['context'].clear()
	print "After", request.session['context']
	return redirect('/')