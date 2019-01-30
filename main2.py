from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="home")

# email verification helper function
def emailverification(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
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
    if password != vpasswrd == True:
        vpasswrd_error = "Password doesn't match"
        vpasswrd = ''
    
    # verify email
    if emailverification(email) == False:
        email_error = "Enter a valid email"
        email = ''
        
    #else:
     #   email = email 
      #  if len(email) >20 or len(email) > 3:
       #     email_error = "Email must be between 3 and 20 characters"
        #    email = ''
    

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