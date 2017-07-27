from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

now = datetime.now()

app = Flask(__name__)
app.secret_key = 'ThisIsSecretes'



@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	return render_template("index.html")


@app.route('/process_money',methods=['POST'])
def gold_pot():

	if 'actions' not in session:
		session['actions'] = []
	
	if request.form['action'] == 'Farm':
		new_gold = random.randint(10,20)
		session['gold'] += new_gold
		deed = ("green","Earned %s golds from the farm! (%s/%s/%s %s:%s)" % (new_gold, now.month, now.day, now.year, now.hour, now.minute))
		session['actions'].insert(0,deed)
		return redirect('/')

	if request.form['action'] == 'Cave':
		new_gold = random.randint(5,10)
		session['gold'] += new_gold
		deed = ("green","Earned %s golds from the cave! (%s/%s/%s %s:%s)" % (new_gold, now.month, now.day, now.year, now.hour, now.minute))
		session['actions'].insert(0,deed)
		return redirect('/')

	if request.form['action'] == 'House':
		new_gold = random.randint(2,5)
		session['gold'] += new_gold
		deed = ("green","Earned %s golds from the house! (%s/%s/%s %s:%s)" % (new_gold, now.month, now.day, now.year, now.hour, now.minute))
		session['actions'].insert(0,deed)
		return redirect('/')

	if request.form['action'] == 'Casino':
		new_gold = random.randint(-50,50)
		session['gold'] += new_gold
		outcome = "earned"
		excl = "YEAY"
		color = "green"
		if new_gold < 0:
			outcome = "lost"
			excl = "Ouch"
			color = "red"
		deed = (color,"Entered a casino and %s %s golds... %s..! (%s/%s/%s %s:%s)" % (outcome,new_gold,excl,now.month, now.day, now.year, now.hour, now.minute))
		session['actions'].insert(0,deed)
		return redirect('/')


app.run(debug=True)



