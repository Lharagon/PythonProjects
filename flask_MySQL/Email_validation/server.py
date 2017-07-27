from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'ThisIsSecrete'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emails', methods=['POST'])
def create():
	error = 0
	email_char = request.form['email']
	if len(email_char) < 1:
		flash("Email cannot be blank!")
		error += 1
	elif not email_re.match(email_char):
		flash("Not Valid Email")
		error += 1

	if error > 0:
		return redirect ('/')

	query = "INSERT INTO emails (email, created_at, updated_at) VALUES(:email, NOW(), NOW())"
	data = {'email': request.form['email']}
	mysql.query_db(query, data)
	flash("The email address you entered " + request.form['email'] + " is a valid email address! Thank you!")
	emails = mysql.query_db("SELECT * FROM emails")
	return render_template('success.html', all_emails = emails)

@app.route('/remove', methods=['POST'])
def delete():
	email = request.form['email']
	query = "DELETE FROM emails WHERE email = :email"
	data = {'email': email}
	mysql.query_db(query, data)
	emails = mysql.query_db("SELECT * FROM emails")
	return render_template('success.html', all_emails = emails)


app.run(debug=True)