from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home_page.html', title="signup")

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    if (not username) or (username.strip() == ""):
        error = "That's not a valid username"
        return redirect("/")
    return render_template('welcome_page.html', username=username)

app.run()