from flask import Flask, render_template, request, redirect, flash, session

import re


app = Flask(__name__)
app.secret_key = "Very_Secret"

email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
first_re = re.compile(r'^[a-zA-Z]+$')
last_re = re.compile(r'^[a-zA-Z]+$')
password_re = re.compile(r'^[A-Z][0-9][a-zA-Z0-9.+_-]{8,}.\*?$')


@app.route('/')
def landing():
	return render_template('index.html')



@app.route('/process', methods=["POST"])
def process():


	first = request.form['first_name']
	last = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	passconf = request.form['passconf']

	if len(first) < 1:
		flash("First Name cannot be blank!")
	elif not first_re.match(first):
		flash("Invalid first Name")
	
	if len(last) < 1:
		flash("Last Name cannot be blank!")
	elif not last_re.match(last):
		flash("Invalid last Name")

	if len(email) < 1:
		flash("Email cannot be blank!")
	elif not email_re.match(email):
		flash("Not Valid Email")

	if len(password) < 1:
		flash("Password cannot be blank!")
	elif not password_re.match(password):
		flash("Not a valid password")

	if len(passconf) < 1:
		flash("Please confirm password!")
	elif password != passconf:
		flash("Passwords don't match")

	if len(session) == 0:
		flash("Good Job")

	return redirect('/')

app.run(debug=True)