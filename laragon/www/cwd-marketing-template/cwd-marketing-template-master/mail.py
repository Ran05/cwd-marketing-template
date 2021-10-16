# from flask import Flask, render_template,request
# from flask_mail import Mail,Message

# app = Flask(__name__)



# # parameters required for configuration of email

# app.config['MAIL_SERVER'] = 'smpt.gmail.com' #server using gmail
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'randolfh.cwd@gmail.com'
# app.config['MAIL_PASSWORD'] = 'randolfhcwd123'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

# # route that connect to profile page

# @app.route('/profile.html')
# def index():
#     return render_template('send_message')

# # second route for email server post request
# @app.route('/profile.html', methods=['GET','POST'])
# def send_message():
#     if request.method == "POST":
#         email = request.form['email']
#         subject = request.form['subject']
#         msg = request.form['message']

#         # Now past to email Library
#         message = Message(subject,sender="randolfh.cwd@gmail.com", recipients=[email])
#         message.body = msg

#         # flask sending email method
#         mail.send(message)
#         success = "message has been sent"
#         # After send return to another page
#         return render_template('result.html', success = success)

      






# if __name__ == "__main__":
#  app.run(debug=True)



# # this is config file for email
# # app.config['DEBUG'] = True
# # app.config['TESTING'] = False
# # app.config['MAIL_SERVER'] = 'smpt.gmail.com' #server using gmail
# # app.config['MAIL_PORT'] = 587
# # app.config['MAIL_USE_TLS'] = True
# # app.config['MAIL_USE_SSL'] = False
# # app.config['MAIL_DEBUG'] = True
# # app.config['MAIL_USERNAME'] = 'randolfh.cwd@gmail.com'
# # app.config['MAIL_PASSWORD'] = 'randolfhcwd123'
# # app.config['MAIL_DEFAULT_SENDER'] = 'randolfh.cwd@gmail.com'
# # app.config['MAIL_MAX_EMAILS'] = None
# # app.config['MAIL_SUPPRESS_SEND'] = False
# # app.config['MAIL_ASCII_ATTACHEMENTS'] = False

# #mail application
# # mail = Mail(app)

# #create route for cwd-profile page

# # @app.route('/profile.html')
# # def index():
# #     msg = Message('Hey There', send)

