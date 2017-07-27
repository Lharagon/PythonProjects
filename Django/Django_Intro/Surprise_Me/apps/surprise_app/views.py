from django.shortcuts import render, redirect
from random import randint
VALUES = [
"Life is about making an impact, not making an income. Kevin Kruse",
"Whatever the mind of man can conceive and believe, it can achieve. Napoleon Hill",
"Strive not to be a success, but rather to be of value. Albert Einstein",
"Two roads diverged in a wood, and II took the one less traveled by, And that has made all the difference.  Robert Frost",
"I attribute my success to this: I never gave or took any excuse. Florence Nightingale",
"I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed. Michael Jordan",
"The most difficult thing is the decision to act, the rest is merely tenacity. Amelia Earhart",
"Every strike brings me closer to the next home run. Babe Ruth",
"Definiteness of purpose is the starting point of all achievement. W. Clement Stone",
"Life isn't about getting and having, it's about giving and being. Kevin Kruse",
"We become what we think about. Earl Nightingale",
"Life is 10 percent what happens to me and 90 percent of how I react to it. Charles Swindoll",
"The mind is everything. What you think you become.  Buddha",
"The best time to plant a tree was 20 years ago. The second best time is now. Chinese Proverb",
"An unexamined life is not worth living. Socrates",
"Eighty percent of success is showing up. Woody Allen",
"I am not a product of my circumstances. I am a product of my decisions. Stephen Covey",
"Every child is an artist.  The problem is how to remain an artist once he grows up. Pablo Picasso",
"You can never cross the ocean until you have the courage to lose sight of the shore. Christopher Columbus"
]

def index(request):
	if 'context' in request.session:
		request.session['context'].pop(0)
		request.session['num'] = None
	return render(request, 'surprise_app/index.html')

def results(request):

	return render(request, 'surprise_app/results.html')


def process(request):
	request.session['num'] = request.POST['number']
	choice = request.session['num']
	quotes = []

	for times in range(int(choice)):
		quotes.append(VALUES[randint(0,len(VALUES))])

	request.session['context'] = quotes

	return redirect('/results')








