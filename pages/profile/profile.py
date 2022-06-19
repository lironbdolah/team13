from flask import Blueprint, render_template, request, redirect
from utilities.DB.db_manager import interact_db
import mysql.connector

# profile blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile',
                    template_folder='templates')


# Routes
@profile.route('/profile', methods=['GET', 'POST'])
def redirect_profile():
    return render_template('profileHTML.html')


@profile.route('/profile/searchInput')
def redirect_profile_searchInput():
    business_name = request.args['searchInput']

    query = "SELECT * FROM businesses WHERE name='%s';" % business_name
    business = interact_db(query, 'fetch')

    business_row = business[0]
    business_deals = business_row.deals.split('$')
    print(business_deals)

    return render_template('profileHTML.html', business={
        'title': business_row.name,
        'start_hour': business_row.start_hour,
        'end_hour': business_row.end_hour,
        'deals': business_deals,
        'stars': business_row.stars,
        'url': business_row.url
    })
