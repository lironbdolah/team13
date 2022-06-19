from flask import Blueprint, render_template, request, redirect
import mysql.connector

# home blueprint definition
home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')

# Routes
@home.route('/home')
def redirect_home():
    return render_template('homeHTML.html')
