from flask import Flask, request, render_template
from smtplib import SMTP;
from os import getenv;

app = Flask(__name__)

@app.route('/')
def index():
    # name = request.args.get('name', 'World') # GET
    # name = request.form.get('name', 'World') # FORM
    name = 'World'

    # return redirect('/ROUTE_HERE')
    return render_template('index.html', name=name)

@app.route('/send')
def send():
    email = request.form.get('email')
    message = request.form.get('message')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aldrintaylormail@gmail.com', os.getenv('PASSWORD')) # Logging In
    server.sendmail('aldrintaylormail@gmail.com', email, message) # Sending Email

    return 'Success!'
