from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mail import Mail, Message
import requests
import smtplib

app = Flask(__name__)


with app.app_context():
    app.debug = True
    app.config['SECRET_KEY'] = 'EO)BJRS0azcAqW10P"1lJqUcV'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'mmcw.emailbot@gmail.com'
    app.config['MAIL_DEFAULT_SENDER'] = 'Email bot'
    app.config['MAIL_PASSWORD'] = 'FGob`7fQ1rGgIF,oEQBSt4Ytb'

mail = Mail(app)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        content = request.form['message']
        msg = Message(f'New message from {name}', sender=f"{email}",
                      recipients=['michaelmcwong@hotmail.co.uk'])
        msg.body = f'Sent from {email}: \n\n' + content
        mail.send(msg)
        return redirect('/thankyou.html')
    else:
        return 'something has gone wrong'
