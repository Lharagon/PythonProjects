from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

now = datetime.now()

# Create your views here.
def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	return render(request, 'gold_app/index.html')

def process(request):

	if 'actions' not in request.session:
		request.session['actions'] = []

	if request.POST['action'] == 'Farm':
		new_gold = random.randint(10,20)
		request.session['gold'] += new_gold
		deed = ("green","Earned %s golds from the farm! (%s/%s/%s %s:%s)" % (new_gold, now.month, now.day, now.year, now.hour, now.minute))
		request.session['actions'].insert(0,deed)
		return redirect('/')

	if request.POST['action'] == 'Cave':
		new_gold = random.randint(5,10)
		request.session['gold'] += new_gold
		deed = ("green","Earned %s golds from the cave! (%s/%s/%s %s:%s)" % (new_gold, now.month, now.day, now.year, now.hour, now.minute))
		request.session['actions'].insert(0,deed)
		return redirect('/')

	if request.POST['action'] == 'House':
		new_gold = random.randint(2,5)
		request.session['gold'] += new_gold
		deed = ("green","Earned %s golds from the house! (%s/%s/%s %s:%s)" % (new_gold, now.month, now.day, now.year, now.hour, now.minute))
		request.session['actions'].insert(0,deed)
		return redirect('/')

	if request.POST['action'] == 'Casino':
		new_gold = random.randint(-50,50)
		request.session['gold'] += new_gold
		outcome = "earned"
		excl = "YEAY"
		color = "green"
		if new_gold < 0:
			outcome = "lost"
			excl = "Ouch"
			color = "red"
		deed = (color,"Entered a casino and %s %s golds... %s..! (%s/%s/%s %s:%s)" % (outcome,abs(new_gold),excl,now.month, now.day, now.year, now.hour, now.minute))
		request.session['actions'].insert(0,deed)
		return redirect('/')
	


