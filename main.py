""" First attempt at making a website from scratch with Flask and Bootstrap. Wish me luck! """

import re
import os
import jinja2
from flask import Flask, request, redirect, render_template, flash
from server.app import app, db
from server.models import ContactForm, User
from server.hashutils import make_pw_hash, check_pw_hash

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

@app.route("/", methods=['GET'])
def home():
    """ This brings up the home page. """
    return render_template("home.html")

@app.route("/about", methods=['GET'])
def about():
    """ This brings up the about page. """
    return render_template("about.html")

@app.route("/portfolio", methods=['GET'])
def portfolio():
    """ This brings up the portfolio page. """
    return render_template("portfolio.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    """ This brings up the contact page. """
    if request.method == "POST":
        flash("This isn't set up yet!", 'error')
        return redirect("/")
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()