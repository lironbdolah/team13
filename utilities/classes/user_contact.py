from utilities.DB.db_manager import DBManager
# from utilities.DB.db_manager import interact_db

class user_contact:
    def __init__(self, name, email, phone_number):
        super().__init__()
        self.user_name = name
        self.user_email = email
        self.phone_number = int(phone_number)

    def add_user_contact(self):
        guery = "INSERT INTO contacts(full_name, email, phone_number) VALUES ('%s', '%s', '%s')" % (self.user_name, self.user_email, self.phone_number)
        db = DBManager()
        db.commit(guery)