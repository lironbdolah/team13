from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

# connect blueprint definition
from utilities.DB.db_manager import DBManager
# from utilities.DB.db_manager import interact_db
from utilities.classes.User import User

connect = Blueprint('connect', __name__, static_folder='static', static_url_path='/connect',
                    template_folder='templates')


# Routes
@connect.route('/connect', methods=['GET', 'POST'])
def redirect_connect():
    message_for_user = ''
    if request.method == "POST":
        user_password = request.form['pass']
        user_email = request.form['email']
        user = User(email=user_email, password=user_password)
        message_connect = user.connect()


        if(message_connect == 'משתמש נכנס בהצלחה'):
            session['logedin'] = True
            session['user_email'] = user_email
            return redirect('/home')

        elif(message_connect == 'הסיסמה לא תואמת לאימייל, אנא נסה בשנית!'):
             return render_template('connect.html', message_for_user=message_connect)

        else:
            return render_template('connect.html', message_for_user=message_connect)


    return render_template('connect.html', message_for_user=message_for_user)

@connect.route('/connect/delete-user', methods=['GET', 'POST'])
def delete_user():
    message_delete = ''
    if request.method == "POST":
        user_password = request.form['pass']
        user_email = request.form['email']
        user = User(email=user_email, password=user_password)

        if user.delete_user():
            message_delete = "משתמש נמחק בהצלחה"
            return render_template('delete_user.html', message_for_user=message_delete)
        message_delete = 'פרטי משתמש לא נמצאו, בדוק אימייל וסיסמה'
    return render_template('delete_user.html', message_for_user=message_delete)



@connect.route('/logout', methods=['GET', 'POST'])
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect('/preview')

