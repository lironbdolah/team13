from flask import Blueprint, render_template, request, redirect
from utilities.classes.user_contact import user_contact
import mysql.connector

# contact blueprint definition
from utilities.DB.db_manager import DBManager
# from utilities.DB.db_manager import interact_db

contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')

# Routes
@contact.route('/contact', methods=['GET', 'POST'])
def redirect_contact():
    if request.method == 'POST':
        contact_name = request.form['fname']
        contact_email = request.form['email']
        contact_phone_number = request.form['phoneNumber']
        contact = user_contact(contact_name, contact_email, contact_phone_number)
        contact.add_user_contact()
        return render_template('/contactHTML.html', message_contact= 'תודה על השארת הפרטים, ניצור קשר בהקדם האפשרי')
    else:
        return render_template('/contactHTML.html')
#
#
