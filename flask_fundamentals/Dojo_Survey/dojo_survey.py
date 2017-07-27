from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def landing():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_name():
	name = request.form["name"]
	city = request.form["city"]
	language = request.form["language"]
	comment = request.form["comment"]

	return render_template('results.html', name=name,city=city,language=language,comment=comment)

app.run(debug=True)