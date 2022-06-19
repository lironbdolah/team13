from flask import Blueprint, render_template, request, redirect
import mysql.connector

# project blueprint definition
project = Blueprint('project', __name__, static_folder='static', static_url_path='/project', template_folder='templates')

# Routes
@project.route('/project')
def redirect_project():
    return render_template('projectHTML.html')
