from flask import Blueprint, render_template, request, session
from utilities.classes.User import User
import mysql.connector

# sign_up blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')

# Routes
@sign_up.route('/sign_up', methods=['GET', 'POST'])
def redirect_sign_up():
    message_for_user = ''
    if request.method == "POST":
        user_email = request.form['mail2']
        user = User(user_email)
        message_connect = user.connect_first_time()

        if (message_connect == 'אימייל זה כבר קיים במערכת. אנא בחר אימייל אחר'):
            return render_template('sign_up.html', message_for_user=message_connect)

        else:
            user_email = request.form['mail2']
            user_name = request.form['username2']
            user_password = request.form['password1']
            user_phone = request.form['phone1']
            user_age = request.form['age_label1']
            user_gender = request.form['gender_label1']
            user = User(user_email, user_name, user_password, user_phone, user_age, user_gender)
            user.add_user()
            session['logedin'] = True
            return render_template('homeHTML.html', message_for_user=message_connect)

    return render_template('sign_up.html')