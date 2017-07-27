from django.shortcuts import render, HttpResponse
from random import randint

# Create your views here.
def index(request):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers = "0123456789"
	random_word = ""

	for letter in range(14):
		choice = randint(1,2)
		if choice == 1:
			random_word += alphabet[randint(0,25)]
		else:
			random_word += numbers[randint(0,9)]

	if 'attempt' not in request.session:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] += 1

	context = {
		'random_word': random_word,
	}

	return render(request, 'random_app/index.html', context)