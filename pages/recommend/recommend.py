from flask import Blueprint, render_template, request, redirect
import mysql.connector

# recommend blueprint definition
recommend = Blueprint('recommend', __name__, static_folder='static', static_url_path='/recommend', template_folder='templates')

# Routes
@recommend.route('/recommend')
def redirect_recommend():
    return render_template('recommend.html')
