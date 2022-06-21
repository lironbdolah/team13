from flask import Blueprint, render_template, request, redirect
import mysql.connector

# contact blueprint definition
from utilities.DB.db_manager import interact_db

contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')

# Routes
@contact.route('/contact', methods=['GET', 'POST'])
def redirect_contact():
    if request.method == 'POST':
        contact_name = request.form['fname']
        contact_email = request.form['email']
        contact_phone_number = request.form['phoneNumber']
        query = "INSERT INTO contacts(full_name, email, phone_number) VALUES ('%s', '%s', '%s')" % (
        contact_name, contact_email, contact_phone_number)
        interact_db(query, 'commit')
        return render_template('/contactHTML.html')
    else:
        return render_template('/contactHTML.html')


