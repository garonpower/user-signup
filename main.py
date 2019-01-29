from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home_page.html', title="signup")

def is_emtpy(user_input):
    if (not user_input) or (user_input.strip() == ""):
        return True
    else:
        return False

@app.route("/", methods=['POST'])
def validate_input():
    username = request.form['username']

    username_error = ''
    
    if not is_emtpy(username) == True:
        username_error = "That's not a valid username"
        username = ''
    else:        
        if len(username) > 20 or len(username) < 3:
            username_error = "Username must be between 3 and 20 characters"
            username = ''

    if not username_error:
        return redirect('/?username={0}'.format(username))
    else:
        return render_template("/home_page.html", 
            username_error=username_error)


@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return redirect('/')

app.run()