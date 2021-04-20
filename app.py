from flask import Flask , render_template, redirect, request
from forms import loginForm
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '1jhghml'

@app.route('/')
def home():
	return "<center><h1>Welcome</h1></center>"

@app.route('/login', methods=['GET', 'POST'])
def log():
	form = loginForm()
	return render_template ('login.html', form = form)

@app.route('/signin', methods=['GET', 'POST'])
def sign():
	form = loginForm()
	if form.validate_on_submit():
		return request.form['firstname']
		return redirect ('login')
	return render_template('signin.html', form = form, title = 'SignIn')

if __name__ == '__main__':
	app.run()