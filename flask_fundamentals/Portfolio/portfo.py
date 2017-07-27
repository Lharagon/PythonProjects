from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def portfolio():
	return render_template('myPortfolio.html')

@app.route('/projects')

def projects():
	return render_template('aWebPage.html')

@app.route('/about')
def me():
	return render_template('aboutMe.html')

app.run(debug=True)