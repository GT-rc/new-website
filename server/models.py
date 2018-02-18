""" Model Classes """

from app import db
from hashutils import make_pw_hash

class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False)
    name = db.Column(db.String(120))
    message = db.column(db.String(5000))

    def __init__(self, email, name, message):
        self.email = email
        self.name = name
        self.message = message

    def __repr__(self):
        return f'{self.name}\n{self.email}\n{self.message}'

class User(db.Model):
    """ This will be the User class and will hold information regarding user accounts. """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)  # will not allow the same username twice
    user_email = db.Column(db.String(120), unique=True)  # will not allow a user to register twice with the same email address
    pwd_hash = db.Column(db.String(300))

    def __init__(self, username, user_email, password):
        self.username = username
        self.user_email = user_email
        self.pwd_hash = make_pw_hash(password)

    def __repr__(self):
        return f'{self.username}'
"""
    def change_password(self, new_password):  # TODO: Check this - feels like won't work w/ db
        self.password = make_pw_hash(new_password)

    def change_email(self, new_email):
        self.user_email = new_email
"""
