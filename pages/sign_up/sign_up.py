from flask import Blueprint, render_template, request
from utilities.classes.User import User
import mysql.connector

# sign_up blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')

# Routes
@sign_up.route('/sign_up', methods=['GET', 'POST'])
def redirect_sign_up():
    if request.method == "POST":
        user_email = request.form['mail2']
        user_name = request.form['username2']
        user_password = request.form['password1']
        user_phone = request.form['phone1']
        user_age = request.form['age_label1']
        user_gender = request.form['gender_label1']
        print(user_name, user_email, user_password, user_phone, user_age, user_gender)
        user = User(user_email, user_name, user_password, user_phone, user_age, user_gender)
        user.add_user()
    return render_template('sign_up.html')
