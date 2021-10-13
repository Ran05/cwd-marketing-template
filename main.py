# from logging import info
from flask import Flask, render_template,request, redirect, sessions, url_for, session
from flask_mysqldb import MySQL     #flask_mysqldb import MySQL
import MySQLdb 



#connection with the database.
#Im using this sql local server
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
            if info is not None:
                if info ['username'] == username and info ['password'] == password:
                    return render_template('profile.html')
            else:
                return render_template('missinginfo.html')



    return render_template('login.html')



if __name__ ==  '__main__':
    app.run(debug=True)



