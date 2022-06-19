from flask import Blueprint, render_template, request, redirect
import mysql.connector

# connect blueprint definition
connect = Blueprint('connect', __name__, static_folder='static', static_url_path='/connect', template_folder='templates')

# Routes
@connect.route('/connect')
def redirect_connect():
    return render_template('connect.html')
