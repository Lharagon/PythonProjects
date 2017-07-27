from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'ThisIsSecrete'



@app.route('/')

def index():
	if counter not in session:
		session['counter'] = 0
	session['counter'] += 1
	return render_template("index.html", counter = session['counter'])

@app.route('/addTwo', methods=['POST'])
def add():
	session['counter'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] -= session['counter']
	return redirect('/')

app.run(debug=True)