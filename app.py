from flask import Flask , render_template, redirect, request
from forms import loginForm
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from config import Config

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '1jhghml'

@app.route('/')
def home():
	return render_template('welcome.html')

@app.route('/choose')
def choose():
	return render_template('choose.html')	

@app.route('/multiplication')
def multiplication():
	return render_template('multiplication.html')

@app.route('/division')
def division():
	return render_template('division.html')

@app.route('/login', methods=['GET', 'POST'])
def log():
	form = loginForm()
	if form.validate_on_submit():
		return redirect ('choose')
	return render_template ('login.html', form = form) 

@app.route('/signin', methods=['GET', 'POST'])
def sign():
	form = loginForm()
	if form.validate_on_submit():
		return redirect ('login')
		u = models.user(firstname = request.user['firstname'])
		db.session.add(u)
	return render_template('signin.html', form = form, title = 'SignIn')

if __name__ == '__main__':
	app.run(port = app.config['PORT'], debug = app.config['DEBUG'])