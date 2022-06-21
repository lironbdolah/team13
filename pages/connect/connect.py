from flask import Blueprint, render_template, request, redirect
import mysql.connector

# connect blueprint definition
from utilities.DB.db_manager import interact_db

connect = Blueprint('connect', __name__, static_folder='static', static_url_path='/connect',
                    template_folder='templates')


# Routes
@connect.route('/connect', methods=['GET', 'POST'])
def redirect_connect():
    message_for_user =''
    if request.method == "POST":
        user_password = request.form['pass']
        user_email = request.form['email']

        query = 'select * from users'
        users_l = interact_db(query, query_type='fetch')

        message_for_user = 'משתמש נרשם בהצלחה!'
        for user in users_l:
            if user.mail == user_email:
                if user.password == user_password:
                    return render_template('homeHTML.html')
                else:
                    return render_template('connect.html', message_for_user='הסיסמה לא תואמת לאימייל, אנא נסה בשנית!')
        message_for_user='אימייל זה לא קיים במערכת'

    return render_template('connect.html', message_for_user=message_for_user)




