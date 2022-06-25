import math
from utilities.DB.db_manager import DBManager


class Review:
    def __init__(self, review_time='1', stars='-1', free_text='-1', mail='-1', business='-1'):
        self.review_time = review_time
        self.stars = int(stars)
        self.free_text = free_text
        self.mail = mail
        self.business = int(business)
        self.db = DBManager()

    def get_review(self):
        query = "SELECT * FROM reviews WHERE business='%s';" % self.business
        return self.db.fetch(query)

    def insert_review(self):
        query = "INSERT INTO reviews(review_time, stars, free_text, mail, business) VALUES ('%s', '%s', '%s', '%s', '%s')"  % (self.review_time, self.stars, self.free_text, self.mail, self.business)
        return self.db.commit(query)

    def get_avg_stars(self):
        query = "SELECT AVG(stars) as avg_stars FROM reviews WHERE business='%s';" % self.business
        business_avg = self.db.fetch(query)[0].avg_stars
        return math.ceil(business_avg)







