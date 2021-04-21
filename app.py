from flask import Flask , render_template, redirect, request
from forms import loginForm
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from config import config

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '1jhghml'
db = SQLAlchemy(app)
migrate = Migrate(db, app)

@app.route('/')
def home():
	return render_template('welcome.html')
@app.route('/login', methods=['GET', 'POST'])
def log():
	form = loginForm()
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
	app.run()