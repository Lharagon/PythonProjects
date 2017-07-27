from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
mysql = MySQLConnector(app,'Login_users')
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
fn_re = re.compile(r'^[a-zA-Z]{1,}$')
ln_re = re.compile(r'^[a-zA-Z]{1,}$')
pa_re = re.compile(r'^[a-zA-Z0-9]{7,}$')
app.secret_key = 'ThisIsSecrete'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def create():
	error = 0
	

	if request.form['action'] == 'register':
		first = request.form['first_name']
		last = request.form['last_name']
		email = request.form['email']
		password = request.form['password']
		passconf = request.form['passconf']

		query = "SELECT email FROM users WHERE email = :email"
		data = {'email': email}
		response = mysql.query_db(query, data)
		
		if len(response) > 0:
			flash("User Already Taken")

		if len(first) < 1:
			flash("First Name cannot be blank!")
			error += 1
		elif not fn_re.match(first):
			flash("Invalid first Name")
			error += 1
		
		if len(last) < 1:
			flash("Last Name cannot be blank!")
			error += 1
		elif not ln_re.match(last):
			flash("Invalid last Name")
			error += 1

		if len(email) < 1:
			flash("Email cannot be blank!")
			error += 1
		elif not email_re.match(email):
			flash("Not Valid Email")
			error += 1

		if len(password) < 1:
			flash("Password cannot be blank!")
			error += 1
		elif not pa_re.match(password):
			flash("Not a valid password")
			error += 1

		if len(passconf) < 1:
			flash("Please confirm password!")
			error += 1
		elif password != passconf:
			flash("Passwords don't match")
			error += 1

		if error > 0:
			return redirect ('/')
		else:
			query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES(:first_name,:last_name,:email,:password, NOW(), NOW())"
			data = {'first_name': first, 'last_name': last, 'email': email, 'password': md5.new(password).hexdigest()}
			mysql.query_db(query, data)
			flash("Thank you for Registering, please log in.")
			return redirect ('/')

	elif request.form['action'] == 'login':
		email = request.form['email']
		password = request.form['password']
		query = "SELECT * FROM users WHERE email = :email"
		data = {'email': email}
		response = mysql.query_db(query, data)
		if len(response) == 0:
			flash("User Not in database")
			return redirect ('/')

		if response[0]['email'] == email:
			if response[0]['password'] == md5.new(password).hexdigest():
				session['user'] = response[0]['id']
				print session['user']
				return redirect ('/success')
			else: 
				flash("not correct pass")
				return redirect ('/')
		flash("Email not in our Database")
		return redirect ('/')


@app.route('/success')
def success():
	query = "SELECT * FROM users WHERE id = :id"
	data = {'id': session['user']}
	response = mysql.query_db(query, data)
	name = response[0]['first_name']

	return render_template('/success.html', name = name)


app.run(debug=True)