from flask import Blueprint, render_template, request, redirect
import mysql.connector

# profile blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')

# Routes
@profile.route('/profile', methods=['GET', 'POST'])
def redirect_profile():
    return render_template('profileHTML.html')
