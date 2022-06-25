from flask import Blueprint, render_template, request, jsonify, session
from utilities.DB.db_manager import DBManager
import mysql.connector
from datetime import datetime, time
from math import sin, cos, sqrt, atan2, radians
import json

from utilities.classes.Business import Business
from utilities.classes.Review import Review

# profile blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', url_prefix='/profile',
                    template_folder='templates')

# if check time is between begin time and end time -> returns TRUE
def is_time_between(my_begin_time, my_end_time, business_start_time,business_end_time):
    return (my_begin_time >= business_start_time) and (my_end_time <= business_end_time)

def messure_distance(lat1, long1, lat2, long2):
    # approximate radius of earth in km
    R = 6373.0

    dlong = radians(long2-long1)
    dlat = radians(lat2-lat1)

    # a = sin(dlat / 2) * 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) * 2

    a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlong/2) * sin(dlong/2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


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
    city = request.args['combo1']
    hours = request.args['combo2'].split('-')
    times = [i.split(':') for i in hours]

    # # get all businesses in beer sheva
    b = Business()
    b.city = city
    businesses = b.get_future_business()
    good_businesses = []

    # get all businesses who match the time condition and insert them to the list  good_businesses
    for i in businesses:
        business_start_hour = str(i.start_hour).split(':')
        business_end_hour = str(i.end_hour).split(':')
        if is_time_between(time(int(times[0][0]),int(times[0][1])), time(int(times[1][0]), int(times[1][1])),
                           time(int(business_start_hour[0]),int(business_start_hour[1])),time(int(business_end_hour[0]),int(business_end_hour[1]))):
            good_businesses.append(i)

    urls = [i.url for i in good_businesses]
    titles = [i.name for i in good_businesses]
    if len(urls) > 0:
        return render_template('recommend.html', sites=zip(urls, titles))
    else:
        urls.append('home.html')
        titles.append("לא נמצאו בתי עסק ברדיוס שביקשת")
        return render_template('recommend.html', sites=zip(urls, titles))

@profile.route('/by-location', methods=['GET', 'POST'])
def redirect_profile_by_location():
    data = request.get_data().decode('UTF-8')
    json_acceptable_string = data.replace("'", "\"")
    dict = json.loads(json_acceptable_string)

    # get businesses from db:
    b = Business()
    businesses = b.get_all_businesses()

    # user entered variables
    lat_1 = float(dict['latitude'])
    long_1 = float(dict['longitude'])
    range = int(dict['userRange'])
    print("my location:")
    print(lat_1,long_1)

    good_businesses = []
    # get all businesses that are in range:
    for i in businesses:
        lat_2 = i.latitude
        long_2 = i.longitude
        print(lat_2,long_2)
        distance = messure_distance(lat_1, long_1, lat_2, long_2)
        print(distance, range)
        if distance < range:
            good_businesses.append(i)

    urls = [i.url for i in good_businesses]
    titles = [i.name for i in good_businesses]

    if len(titles) > 0:
        return render_template('recommend.html', sites=zip(urls, titles))
    else:
        print("inside")
        urls.append('home.html')
        titles.append("לא נמצאו בתי עסק ברדיוס שביקשת")
        return render_template('recommend.html', sites=zip(urls, titles))


@profile.route('/rank', methods=["POST"])
def rank_business():
    num_of_stars = request.get_json()["numOfStars"]
    text = request.get_json()["textValue"]
    business_id = session["b_id"]

    review = Review(review_time=datetime.now(), stars=num_of_stars, free_text=text, business=business_id, mail="ADIRIS@GMAIL.COM")
    review.insert_review()
    business_new_stars_avg = review.get_avg_stars()

    business_updated = Business(id=business_id)
    business_row = business_updated.get_business_by_id()[0]
    business_deals = business_row.deals.split('$')
    business_updated.update_business_stars(business_new_stars_avg)


    return render_template('profileHTML.html', business={
        'id': business_id,
        'title': business_row.name,
        'start_hour': business_row.start_hour,
        'end_hour': business_row.end_hour,
        'deals': business_deals,
        'stars': business_new_stars_avg,
        'url': business_row.url,
        'reviews': review.get_review()
    })
