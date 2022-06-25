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
        query = 'select * from users'
        users_l = self.db.fetch(query)
        for user in users_l:
            if user.mail == self.email:
                if user.password == self.password:
                    return 'משתמש נכנס בהצלחה'
                else:
                    return 'הסיסמה לא תואמת לאימייל, אנא נסה בשנית!'
        return 'אימייל זה לא קיים במערכת'

    def connect_first_time(self):
        query = 'select * from users'
        users_l = self.db.fetch(query)
        for user in users_l:
            if user.mail == self.email:
                    return 'אימייל זה כבר קיים במערכת. אנא בחר אימייל אחר'
            else:
                    return ''
        return ''

