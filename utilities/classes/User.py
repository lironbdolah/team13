from utilities.DB.db_manager import DBManager
# from utilities.DB.db_manager import interact_db


class User:
    def __init__(self, email, user_name='-1', password='-1', phone_number='-1', age='-1', gender='-1'):
        self.email = email
        self.user_name = user_name
        self.password = password
        self.phone_number = int(phone_number)
        self.age = int(age)
        self.db = DBManager()
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
        self.db.commit(query)

    def connect(self):
        query = "SELECT mail FROM users WHERE mail='%s' AND password='%s';" % (self.email, self.password)
        users_l = self.db.fetch(query)
        print(users_l)
        if len(users_l) > 0:
            return 'משתמש נכנס בהצלחה'

        return 'משתמש זה לא קיים במערכת, אנא בדוק את הפרטים בשנית'

    def connect_first_time(self):
        query = "SELECT mail FROM users WHERE mail='%s';" % self.email
        users_l = self.db.fetch(query)
        if len(users_l) > 0:
            return 'אימייל זה כבר קיים במערכת. אנא בחר אימייל אחר'
        return ''

    def delete_user(self):
        print(self.email, self.password)
        query = "DELETE FROM reviews WHERE mail='%s';" % self.email
        self.db.commit(query)
        query = "DELETE FROM users WHERE mail='%s' AND password='%s';" % (self.email, self.password)
        return self.db.commit(query)
