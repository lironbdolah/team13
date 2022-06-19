from flask import Blueprint, render_template, request, redirect
import mysql.connector

# month_reccomendation blueprint definition
month_reccomendation = Blueprint('month_reccomendation', __name__, static_folder='static', static_url_path='/month_reccomendation', template_folder='templates')

# Routes
@month_reccomendation.route('/month_reccomendation')
def redirect_month_reccomendation():
    return render_template('month_reccomendation.html')
