# from logging import info
from flask import Flask, render_template,request, redirect, sessions, url_for, session
from flask_mysqldb import MySQL     #flask_mysqldb import MySQL
import MySQLdb 

app = Flask(__name__)
app.secret_key = "canadianwebdesigns!!@"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "login"




db = MySQL(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':    
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,password,))
            info = cursor.fetchone()
            if info ['username'] == username and info ['password'] == password:
                return render_template('profile.html')
            else:
                return "Login Unsuccessful, Please register again"



    return render_template('login.html')



if __name__ ==  '__main__':
    app.run(debug=True)



























# from flask import Flask, render_template

# app = Flask(__name__)


# ''' Route for login page'''
# @app.route('/')

# def index():
#     return render_template("login.html")

# ''' Route for register page'''

# @app.route('/register.html')

# def new_profile():
#     return render_template("register.html")

# # Route for profile page
# @app.route('/new')

# def profile():
#     return render_template("profile.html")



# if __name__ == '__main__':
#     app.run(debug=True)



