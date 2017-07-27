from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def landing():
	return render_template('index.html')

@app.route('/ninja')
def all():
	ninja = "tmnt.png"
	return render_template('pictures.html', ninja = "../static/Ninjas/"+ninja) 

@app.route('/ninja/<holder>')
def get_name(holder):
	if holder == "blue":
		ninja = "leonardo.jpg"
	elif holder == "orange":
		ninja = "michelangelo.jpg"
	elif holder == "red":
		ninja = "raphael.jpg"
	elif holder == "purple":
		ninja = "donatello.jpg"
	else:
		ninja = "notapril.jpg"


	return render_template('pictures.html', ninja = "../static/Ninjas/"+ninja)

app.run(debug=True)