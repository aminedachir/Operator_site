import os
basedir = os.path.abspath(os.path.dirname(__file__))
class config(object):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
	'sqlite:///' + os.path.join(basedir,'app.db')
	SECRET_KEY = os.environ.get('SECRET_KEY') or '@17lames.com'
	SQLALCHEMY_TRACK_MODIFICATIONS = False