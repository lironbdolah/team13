from utilities.DB.db_manager import DBManager


class Review:
    def __init__(self, review_time='-1', stars='-1', free_text='-1', mail='-1', business='-1'):
        self.review_time = review_time
        self.stars = int(stars)
        self.free_text = free_text
        self.mail = mail
        self.business = int(business)
        self.db = DBManager()

    def get_review(self):
        query = "SELECT * FROM reviews WHERE business='%s';" % self.business
        return self.db.fetch(query)





