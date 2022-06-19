from flask import Blueprint, render_template, request, redirect
import mysql.connector

# preview blueprint definition
preview = Blueprint('preview', __name__, static_folder='static', static_url_path='/preview', template_folder='templates')

# Routes
@preview.route('/preview')
def redirect_preview():
    return render_template('preview.html')
