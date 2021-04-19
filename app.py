from flask import Flask , render_template
from forms import loginForm

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '1jhghml'

@app.route('/')
def home():
	return "<center><h1>Welcome</h1></center>"

@app.route('/login', methods=['GET', 'POST'])
def log():
	form = loginForm()
	return render_template('login.html', form = form, title = 'SignIn')

if __name__ == '__main__':
	app.run()