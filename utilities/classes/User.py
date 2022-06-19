from utilities.DB.db_manager import interact_db


class User:
    def __init__(self, email, user_name, password, phone_number, age, gender):
        super().__init__()
        self.email = email
        self.user_name = user_name
        self.password = password
        self.phone_number = int(phone_number)
        self.age = int(age)
        if(gender == 'זכר'):
            self.gender = 'M'
        elif(gender == 'נקבה'):
            self.gender = 'F'
        else:
            self.gender = 'U'

    def get_mail(self):
        return self.mail

    def set_mail(self, mail):
        self.mail = mail

    def add_user(self):
        query = "INSERT INTO users(mail, user_name, password, phone_number, age, gender) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (self.email, self.user_name, self.password, self.phone_number, self.age, self.gender)
        # self.commit(query)
        interact_db(query, 'commit')


