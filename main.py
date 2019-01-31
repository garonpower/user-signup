from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="home")

# password verification helper function
def passwordverification(password):
    if len(password) > 0:
        for space in password:
            if space == ' ':
                return False
    if len(password) > 20 or len(password) < 3:
        return False

# verify password helper function
def verify_pswrd(vpasswrd):
    if (not vpasswrd) or (vpasswrd.strip() == ""):
        return False
    if len(vpasswrd) > 20 or len(vpasswrd) < 3:
        return False

# email verification helper function
def emailverification(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if len(email) > 20 or len(email) < 3:
        return False
    if match == None:
        return False


@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    vpasswrd = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    vpasswrd_error = ''
    email_error = ''

    # username
    if (not username) or (username.strip() == ""):
        username_error = "That's not a valid username"
        username = ''
    elif len(username) > 0:
        for space in username:
            if space == ' ':
                username_error = "No spaces allowed"
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
        if passwordverification(password) == False:
            password_error = "Your password must be between 3 and 20 characters with no spaces"
            password = ''

    # verify password
    if verify_pswrd(vpasswrd) == False:
        vpasswrd_error = "That's not a valid password"
        vpasswrd = ''
    else:
        vpasswrd = vpasswrd
        if vpasswrd != password:
            vpasswrd_error = "Password doesn't match"
            vpasswrd = ''
    
    # verify email
    while (not email) or (email.strip() == ""):
        break
        if len(email) > 0:
            for space in email:
                if space == " ":
                    email_error = "No spaces alowed"
    else:
        if emailverification(email) == False:
            email_error = "Enter a valid email between 3 & 20 characters long"
            email = ''
        
    # If there are no errors, welcome "username"
    if not username_error and not password_error and not vpasswrd_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('/signup.html', 
            username_error=username_error,
            password_error=password_error,
            vpasswrd_error=vpasswrd_error,
            email_error=email_error,
            username=username,
            email=email)

app.run()