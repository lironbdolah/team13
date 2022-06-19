from flask import Blueprint, render_template, request, redirect
import mysql.connector

# contact blueprint definition
contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')

# Routes
@contact.route('/contact')
def redirect_contact():
    return render_template('contactHTML.html')
