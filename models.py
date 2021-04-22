from app import db

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(120))
	lastname = db.Column(db.String(120))
	email = db.Column(db.String(120))
	confirm_email = db.Column(db.String(120))
	password = db.Column(db.String(120))
	confirm_password = db.Column(db.String(120))

	def __repr__(self):
		return f"<user {self.firstname}>"
