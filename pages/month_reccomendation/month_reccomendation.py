from flask import Blueprint, render_template, request, redirect
import mysql.connector

# month_reccomendation blueprint definition
from utilities.classes.Business import Business

month_reccomendation = Blueprint('month_reccomendation', __name__, static_folder='static', static_url_path='/month_reccomendation', template_folder='templates')

# Routes
@month_reccomendation.route('/month_reccomendation')
def redirect_month_reccomendation():
    b = Business()
    businesses = b.month_businesses()
    print(businesses)

    return render_template('month_reccomendation.html', businesses={
        'first': businesses[0].name,
        'first_url': businesses[0].url,
        'second': businesses[1].name,
        'second_url': businesses[1].url,
        'third': businesses[2].name,
        'third_url': businesses[2].url})
