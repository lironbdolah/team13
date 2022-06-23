from flask import Blueprint, render_template, request, jsonify, session
from utilities.DB.db_manager import DBManager
import mysql.connector

from utilities.classes.Business import Business
from utilities.classes.Review import Review

# profile blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', url_prefix='/profile',
                    template_folder='templates')


# Routes
@profile.route('/', methods=['GET', 'POST'])
def redirect_profile():
    return render_template('profileHTML.html')


@profile.route('/searchInput')
def redirect_profile_searchInput():
    business_name = request.args['searchInput']

    b = Business(name=business_name)
    business = b.get_business()
    business_row = business[0]

    business_deals = business_row.deals.split('$')

    r = Review(business=business_row.id)
    review = r.get_review()
    #  = review.get_review(id=business_row.id)
    # print(review_list)
    session['b_id'] = business_row.id

    return render_template('profileHTML.html', business={
        'id': business_row.id,
        'title': business_row.name,
        'start_hour': business_row.start_hour,
        'end_hour': business_row.end_hour,
        'deals': business_deals,
        'stars': business_row.stars,
        'url': business_row.url,
        'reviews': review
    })


@profile.route('/futureSearch')
def redirect_profile_future_search():
    print(request.args)
    return render_template('homeHtml.html')


@profile.route('/by-location', methods=["POST"])
def redirect_profile_by_location():
    print(request.get_data())
    return jsonify({"test": 1})


@profile.route('/rank', methods=["POST"])
def rank_business():
    print(request.get_data())
    # TODO missing profile update before render template
    # TODO missing code protection on missing business inside template
    return render_template('profileHTML.html')
