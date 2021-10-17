# from logging import info
from flask import Flask, render_template,request, redirect, sessions, url_for, session
from flask_mysqldb import MySQL     #flask_mysqldb import MySQL
from flask_mail import Mail,Message
import MySQLdb 

#connection with the database.
#Im using this sql local server

app = Flask(__name__)
app.secret_key = "canadianwebdesigns!!@"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "login"

# parameters required for configuration of email

app.config['MAIL_SERVER'] = 'smpt.gmail.com' #server using gmail
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'randolfh.cwd@gmail.com'
app.config['MAIL_PASSWORD'] = 'randolfhcwd123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db = MySQL(app)
mail = Mail(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':    
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,password,))
            info = cursor.fetchone()
            if info is not None:
                if info ['username'] == username and info ['password'] == password:
                    return render_template('profile.html')
            else:
                return render_template('missinginfo.html')
    return render_template('login.html')

#Route for profile page
@app.route('/profile')
def index1():
    return render_template('send_message')

# second route for email server post request
@app.route('/profile', methods=['GET','POST'])
def send_message():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        # Now past to email Library
        message = Message(subject,sender="randolfh.cwd@gmail.com", recipients=[email])
        message.body = msg

        # flask sending email method
        mail.send(message)
        success = "message has been sent"
        # After send return to another page
        return render_template('profile.html', success = success)

if __name__ ==  '__main__':
    app.run(debug=True)



