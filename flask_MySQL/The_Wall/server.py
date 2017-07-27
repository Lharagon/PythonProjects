from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import datetime

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

# FORM VALIDATION ON INDEX PAGE
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

# MAIN PAGE WHERE THE WALL IS

@app.route('/success')
def success():
	if 'user' not in session:
		flash("Please Log-in or Register")
		return redirect('/')

	print session
	query = "SELECT * FROM users WHERE id = :id"
	data = {'id': session['user']}
	response = mysql.query_db(query, data)
	name = response[0]['first_name']


	query = "SELECT message, messages.id, concat(users.first_name, ' ',users.last_name) AS user, messages.created_at, messages.user_id FROM messages JOIN users ON messages.user_id = users.id ORDER  BY created_at DESC;"
	data = {}
	messages_list = mysql.query_db(query, data)
	#mess_time = datetime.strptime(message['created_at'], "%B %d %Y")

	query = "SELECT comment, message_id, concat(users.first_name, ' ',users.last_name) AS user, comments.created_at FROM comments JOIN users ON users.id = comments.user_id ORDER  BY created_at DESC;"
	data = {}
	comment_list = mysql.query_db(query, data)
	# comm_time = 

	return render_template('/wall.html', name = name, messages_list = messages_list, comment_list= comment_list)

# ROUTE FOR POSTING 

@app.route('/post', methods=['POST'])
def post():
	if request.form['action'] == 'post_message':
		message = request.form['message']
		query = "INSERT INTO messages(message,created_at,updated_at,user_id) VALUES(:message,NOW(), NOW(),:user_id)"
		data = {'message': message, 'user_id': session['user']}
		mysql.query_db(query, data)
		return redirect('/success')

	if request.form['action'] == 'post_comment':
		comment_var = request.form['comment']
		mess_id = request.form['mes_id']
		query = "INSERT INTO comments(message_id,user_id,comment,created_at,updated_at) VALUES(:message,:user_id,:comment,NOW(), NOW())"
		data = {'message': mess_id, 'user_id': session['user'], 'comment': comment_var}
		mysql.query_db(query, data)
	

		print comment_var, mess_id
		return redirect('/success')

# LOGS USERS OUT

@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	print session
	return redirect('/')

# DELETES A MESSAGE POST

@app.route('/delete', methods=['POST'])
def deleteMess():
	query = "DELETE FROM messages WHERE id = :id"
	data = {'id': request.form['deleteMessID']}
	mysql.query_db(query, data)
	return redirect('/success')

app.run(debug=True)