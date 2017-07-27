from flask import Flask, render_template, request, redirect
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM friends")
	return render_template('index.html', all_friends = friends)


@app.route('/friends', methods=['POST'])
def create():
    print request.form['first_name']
    print request.form['last_name']
    # add a friend to the database!
    query = "INSERT INTO friends (first_name, last_name, created_at, updated_at) VALUES (:first_name, :last_name, NOW(), NOW())"
    data = {'first_name': request.form['first_name'],'last_name': request.form['last_name']}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
