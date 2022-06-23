from utilities.DB.db_manager import DBManager


class Business:
    def __init__(self, name='-1', url='-1', password='-1', start_hour='-1', end_hour='-1', deals='-1', stars='-1', city='-1', latitude='-1', longitude='-1'):
        self.url = url
        self.name = name
        self.password = password
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.deals = deals
        self.stars = int(stars)
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.db = DBManager()

    def get_business(self):
        query = "SELECT * FROM businesses WHERE name='%s';" % self.name
        return self.db.fetch(query)





