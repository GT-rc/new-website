""" Model Classes """

from app import db

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