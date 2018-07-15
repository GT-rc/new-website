""" Database Connection """

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('new_website')
app.config['DEBUG'] = True  # Displays runtime errors
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://port-site:questionable@localhost:8889/port-site'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "?JVX^[N:4@=[j6fO;AitNR7V's5VgXq.JT?"
app.template_folder = os.path.join(os.path.dirname(__file__), '../templates')

db = SQLAlchemy(app)
