from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecrete'



@app.route('/')

def index():
	session['counter'] += 1
	if session['counter'] == 1:
		goal = random.randint(1,100)
		session['goal'] = goal
		print goal

	return render_template("index.html")

@app.route('/check',methods=['POST'])

def guess():
	
	guess = int(request.form['answer'])
	print guess
	print session['goal']

	if guess == session['goal']:
		return render_template('won.html')

	if guess < session['goal']:
		return render_template('low.html')

	if guess > session['goal']:
		return render_template('high.html')
	#if guess = session['goal']:
	#	return render_template('index.html')

@app.route('/reset', methods=["POST"])
def reset():
	session['counter'] -= session['counter']
	return redirect('/')


app.run(debug=True)
