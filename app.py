from datetime import timedelta

from flask import Flask, redirect, render_template, url_for, request, session
import mysql.connector

app = Flask(__name__)
# from forms_data import users

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

###### Pages
## home
from pages.home.home import home
app.register_blueprint(home)

## businesses
from pages.businesses.businesses import businesses
app.register_blueprint(businesses)

## connect
from pages.connect.connect import connect
app.register_blueprint(connect)

## contact
from pages.contact.contact import contact
app.register_blueprint(contact)

## month_reccomendation
from pages.month_reccomendation.month_reccomendation import month_reccomendation
app.register_blueprint(month_reccomendation)

## preview
from pages.preview.preview import preview
app.register_blueprint(preview)

## profile
from pages.profile.profile import profile
app.register_blueprint(profile)

## project
from pages.project.project import project
app.register_blueprint(project)

## sign_up
from pages.sign_up.sign_up import sign_up
app.register_blueprint(sign_up)

if __name__ == '__main__':
    app.run(debug=True)