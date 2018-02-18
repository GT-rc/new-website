""" Database Connection """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True  # Displays runtime errors
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://port-site:questionable@localhost:8889/port-site'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
