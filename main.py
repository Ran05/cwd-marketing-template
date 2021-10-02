from flask import Flask, render_template

app = Flask(__name__)


''' Route for login page'''
@app.route('/')

def index():
    return render_template("login.html")

''' Route for register page'''

@app.route('/register.html')

def new_profile():
    return render_template("register.html")

# Route for profile page
@app.route('/new')

def profile():
    return render_template("profile.html")



if __name__ == '__main__':
    app.run(debug=True)