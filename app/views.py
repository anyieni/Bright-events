import re
from app import app
from flask import render_template, redirect, request
from .models.user import User

userData = []


def password_validation(password):
    if len(password) < 8 or re.search("[A-Z]", password) is None or re.search("[0-9]", password) is None:
		return False


@app.route('/')
def index():
	return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST' ])
def register():
	if request.method == "POST":
		user_name = request.form["username"]
		password = request.form["password"]
		password2 = request.form["conf_password"]

		if (password != password2):
			return "passwords do not match"

		if password_validation(password) is False:
			return "password should be more than eight characters and contain a capital letter and number"

		for user in userData:
			if ( user.user_name == user_name ):
				return "user already exists"

		new_user = User(user_name, password)
		userData.append(new_user)
		return redirect('/login')
	elif request.method == "GET":
		return render_template("signup.html")



@app.route('/login', methods=['GET', 'POST' ])
def login():
    if request.method == "POST":
		user_name = request.form["username"]
		password = request.form["password"]
		for user in userData:
			if ((user.user_name == user_name) and (user.password == password)):
				return render_template("listevents.html")
			else:
				return "username or password does not exist"
    elif request.method == "GET":
		return render_template("login.html")

