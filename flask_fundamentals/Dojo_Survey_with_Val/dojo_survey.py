from flask import Flask, render_template, request, redirect, flash, get_flashed_messages, url_for
import re
app = Flask(__name__)
app.secret_key = "THIS IS HELLA SECRET"

email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
first_re, last_re = re.compile(r'^[a-zA-Z]+$')


@app.route('/')
def landing():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_name():
	name = request.form["name"]
	city = request.form["city"]
	language = request.form["language"]
	comment = request.form["comment"]

	error = 0

	if len(name) < 1:
			flash("Name cannot be empty")
			error += 1
	if len(comment) < 1:
			flash("Comment cannot be empty")
			error += 1
	if len(comment) > 120:
			flash("Comment cannot be more than 120 characters")
			error += 1

	
	
	if error > 0:
			return redirect('/')


	return render_template('results.html', name=name,city=city,language=language,comment=comment)

app.run(debug=True)