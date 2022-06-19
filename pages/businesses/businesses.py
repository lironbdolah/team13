from flask import Blueprint, render_template, request, redirect, Flask

import mysql.connector

# businesses blueprint definition
businesses = Blueprint('businesses', __name__, static_folder='static', static_url_path='/businesses', template_folder='templates')

# Routes
@businesses.route('/businesses')
def redirect_businesses():
    return render_template('businesses.html')