from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="home")

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    vpasswrd = request.form['verify_password']

    username_error = ''
    password_error = ''
    vpasswrd_error = ''

    # username
    if (not username) or (username.strip() == ""):
        username_error = "That's not a valid username"
        username = ''
    else:
        username = username
        if len(username) > 20 or len(username) < 3:
            username_error = "Username must be between 3 and 20 characters"
            username = ''

    # password
    if (not password) or (password.strip() == ""):
        password_error = "That's not a valid password"
        password = ''
    else:
        password = password
        if len(password) > 20 or len(password) < 3:
            password_error = "Your password must be between 3 and 20 characters"
            password = ''

    # verify password
    if password != vpasswrd:
        vpasswrd_error = "Password doesn't match"
        vpasswrd = ''
    


    if not vpasswrd_error and not password_error and not password_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('/signup.html', 
            username_error=username_error,
            password_error=password_error,
            vpasswrd_error=vpasswrd_error,
            username=username)

app.run()