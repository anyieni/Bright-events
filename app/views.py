from app import app
from flask import render_template, redirect, request
from .models.user import User

userData = []


@app.route('/')
def index():
	return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST' ])
def register():
	if request.method == "POST":
		user_name = request.form["username"]
		password = request.form["password"]
		new_user = User(user_name, password)
		userData.append(new_user)
		print('--------------------',userData)
		return redirect('/')
	elif request.method == "GET":
		return render_template("signup.html")
