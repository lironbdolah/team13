from utilities.DB.db_manager import DBManager


class InitiateDb:
    def __init__(self):
        self.db = DBManager()

    def create_tables(self):
        query = "SELECT * FROM information_schema.tables WHERE table_schema = 'web-project-g13' AND table_name = 'users';"
        user_list = self.db.fetch(query)
        if len(user_list) == 0:
            query = "CREATE TABLE users (mail VARCHAR(30) not null primary key, user_name VARCHAR(20), password VARCHAR(20), phone_number INTEGER, age INTEGER, gender CHAR(1))"
            self.db.commit(query)
            query = "INSERT INTO users values ('a@gmail.com', 'omerFF', 'anita052A', '524765044', '18', 'F'), " \
                    "('adiri@gmail.com', 'ofiradiri', 'aaasssddDA2', '528129383', '27','M'), " \
                    "('alon@gmail.com', 'alonbr', 'sfjsxjj345KJF', '524765124', '20', 'M')," \
                    " ('liron@gmail.com',	'lironb', 'asdASD123', '520365044',	'26', 'M'), " \
                    "('ofir@gmail.com',	'ofirluke',	'ofirL1122',	'500766783'	,'26',	'F'), " \
                    "('omer@gmail.com', 'omerbenami', 'ASDasd123', '514765044', '20', 'F')"
            self.db.commit(query)

        query = "SELECT * FROM information_schema.tables WHERE table_schema = 'web-project-g13' AND table_name = 'businesses';"
        businesses_list = self.db.fetch(query)
        if len(businesses_list) == 0:
            query = "CREATE TABLE businesses (id INTEGER not null primary key, url VARCHAR(200), name VARCHAR(50), start_hour VARCHAR(10), end_hour VARCHAR(10), stars INTEGER, city VARCHAR(30), longitude FLOAT, latitude FLOAT, deals VARCHAR(500))"
            self.db.commit(query)
            query = "INSERT INTO businesses values ('1', 'https://tabitisrael.co.il/online-reservations/create-reservation?step=search&orgId=610fe6d385269f6b88f6259b&source=facebook', 'פרידה', '19:00', '21:00','3', 'באר שבע', '34.7977', '31.2535','כל היינות 100 שח $ 50% על כל האוכל $ 4 צייסרים ב20 שח' )," \
                    "('2','https://reservations.tabit.cloud/5b792ef60f5e840100cf3a27/booking/search','מילבה','18:00','20:00','4','באר שבע','34.7967','31.2618','30% על כל האוכל $ 50% על כל האלכוהול $ פיצה ב30 שח בלבד')," \
                    "('3', 'https://tabitisrael.co.il/online-reservations/create-reservation?step=search&orgId=6135de3013c3c745fae2acc5&source=website', 'אוללה','17:00','19:00', '4', 'באר שבע', '34.796', '31.2592','1 פלוס 1 על כל האוכל $ בירות ב20 שח בלבד' )," \
                    "('4', 'https://bengimanager.wixsite.com/bengi?fbclid=IwAR1J4KPLs60TDMALFNOExsnXod6z0qXOuxVJjE9Me0b_OygtXX9AhAzv3FE', 'בנגי', '20:00', '21:00', '4', 'באר שבע', '34.7974', '31.2646', '50% הנחה על הבירות מהחבית, היינות והקוקטלים'  )," \
                    "('5', 'http://barshuk.co.il/?fbclid=IwAR0oKm_12Y3UbCjsfNH9QEp96QJ_fm_3gBcA1oIX35z4FDq8a9VFNz7ovVo', 'ברשוק', '20:00', '21:00', '5', 'באר שבע', '34.8002', '31.2676', '50% על הבירות, הצייסרים, כוסות יין וקוקטלים $ בקבוק יין שני ב50% $ עיקריות ב29 שח' )," \
                    "('6', 'https://manga-b7.co.il/?fbclid=IwAR3Z2POJF2baJN-ddCartmQQP17x0I096PvvuDj945njoJ3eO7zxIoGZRLs', 'מנגה', '20:00', '21:00', '2', 'באר שבע', '34.7979', '31.2602','10 צייסרים ב100 שח $ 2 צייסרים ב10 שח בהזמנת בירה מהחבית $ 1+1 על כל הצייסרים' )," \
                    "('7', 'https://www.facebook.com/polalocalpub','פולה', '19:00', '20:00', '2', 'באר שבע', '34.7954', '31.2595', 'כל ההמבורגרים ב20% הנחה')," \
                    "('8',  'https://www.roastersjlm.com/?fbclid=IwAR3ND67vf_SUrHnYUdqfxjCCxC0UmXUOPK1es28QlnCu2Gxvx0qJRHTYEvY', 'רוסטרס', '17:00', '18:00', '3', 'באר שבע', '34.7975', '31.2547', 'קפה ומאפה ב20 שח $ כריך חביתה ב34 שח')," \
                    "('9','https://www.facebook.com/rozzabar', 'רוזה', '19:00', '20:30', '3', 'באר שבע', '34.7952', '31.2594', 'חצי בירה מהחבית פלוס 2 צייסרים 39 שח' )"
            self.db.commit(query)

        query = "SELECT * FROM information_schema.tables WHERE table_schema = 'web-project-g13' AND table_name = 'reviews';"
        reviews_list = self.db.fetch(query)
        if len(reviews_list) == 0:
            query = "CREATE TABLE reviews (review_time datetime not null primary key, stars integer, free_text VARCHAR(200), mail varchar(30), business INTEGER, foreign key (mail) references users (mail),foreign key (business) references businesses (id))"
            self.db.commit(query)
            query = "INSERT INTO reviews values ('2022-05-25 16:15:16', '5', 'מושששש', 'adiri@gmail.com', '1'),('2022-06-18 15:26:29', '2', 'הזמנו שולחן ל10 אנשים, ביקשו מינימום של 70 לראש, איזו חוצפה!', 'liron@gmail.com', '1'),('2022-06-23 16:16:23', '4', 'היה טעים מאוד, אווירה נעימה, נחזור!', 'adiri@gmail.com','2' ),('2022-06-25 13:00:25', '1','מקום גרוע ממש', 'adiri@gmail.com', '1' ),('2022-06-25 17:39:03', '2', 'למה לא חזרתם מאז הקורונה??','a@gmail.com', '6' ),('2022-06-25 19:31:37', '1', 'מקום גרוע', 'a@gmail.com', '4'),('2022-06-25 20:35:04', '4', 'מקום נעים, מוזיקה טובה', 'adiri@gmail.com', '3'),('2022-06-25 20:39:57', '5', 'וואו איזה מקום, פצצוחה!!!','alon@gmail.com', '5'),('2022-06-25 20:40:36', '2','היה לא מפנק בכלל, שילמנו כאילו אנחנו בתל אביב', 'ofir@gmail.com', '7'),('2022-06-25 20:41:36', '5', 'המקום הכי טוב בעולם! פיצה נדירה','omer@gmail.com','8' ),('2022-06-25 20:42:21', '3', 'למה אי אפשר לשלם באפל פיי? מיושנים!!','liron@gmail.com', '9' ),('2022-06-25 20:44:47', '1','מקום גרוע', 'a@gmail.com', '8'),('2022-06-25 20:58:55', '3', 'לא התלהבנו','a@gmail.com','1')"
            self.db.commit(query)

        query = "SELECT * FROM information_schema.tables WHERE table_schema = 'web-project-g13' AND table_name = 'contacts';"
        contacts_list = self.db.fetch(query)
        if len(contacts_list) == 0:
            query = "CREATE TABLE contacts (full_name VARCHAR(50), email VARCHAR(50) not null primary key, phone_number VARCHAR(20))"
            self.db.commit(query)
            query = "INSERT INTO contacts values ('אדירי', 'adiri@gmail.com', '0545864220'),('לירון','liron@gmail.com','0546798420'),('אופיר','ofir@post.bgu.ac.il','0545796420'),('עומר','check@gmail.com','0545746220')"
            self.db.commit(query)
