from utilities.DB.db_manager import interact_db


class Business:
    def __init__(self, url, name, password, start_hour, end_hour, deals, stars, city):
        self.url = url
        self.name = name
        self.password = password
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.deals = deals
        self.stars = int(stars)
        self.city = city

    def get_business(self):
        query = "INSERT INTO users(mail, user_name, password, phone_number, age, gender) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (self.email, self.user_name, self.password, self.phone_number, self.age, self.gender)
        # self.commit(query)
        interact_db(query, 'commit')


