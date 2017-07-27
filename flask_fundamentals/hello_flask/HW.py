from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
	return render_template('index.html')

app.run(debug = True)


#Corresponding html file
'''
<!DOCTYPE html>
<html>
<head>
	<title>Hello Flask</title>
	<style>
		h1 {
			font-size: 110px;
			font-family: Arial;
		}
	</style>
</head>
<body>
	<h1>Hello World!</h1>
	<p>My name is Anna</p>
</body>
</html>
'''