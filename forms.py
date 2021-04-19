from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
	firstname = StringField("First Name", validators=[DataRequired()])
	lastname = StringField("Last name", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	acces = SubmitField("Submit")