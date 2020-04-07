import mysql.connector
from mysql.connector import Error
from user import User

global connection

class Dal:

############################################ methods voor de databaseconnectie
    ## Het openen van een databaseconnectie
    @staticmethod
    def database_connect():
        ##testje
        # try:
            connection = mysql.connector.connect(
              host="localhost",
              database='casus_voorraden',
              user="root",
              passwd="root", auth_plugin='mysql_native_password'
            )

            # if connection.is_connected():
            #     db_Info = connection.get_server_info()
            #     print("Connected to MySQL Server version ", db_Info)
            #     cursor = connection.cursor()
            #     cursor.execute("select database();")
            #     record = cursor.fetchone()
            #     print("You're connected to database: ", record)

            return connection

        # except Error as e:
        #     print("Error while connecting to MySQL", e)

    ## Het sluiten van een databaseconnectie als die open staat
    def database_disconnect(self):
        if connection.is_connected():
            connection.close()
            print("Database is closed")

############################################ einde methods voor de databaseconnectie

    def login_user(self, username):
        connection = self.database_connect()

        sql = "SELECT gebruikersnaam FROM gebruiker where gebruikersnaam like (%s)"

        data = (username,)
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()

        for x in result:
            print(x)

        if result.count != 0:
            print("Welkom, " + username.title())
        else:
            print("Deze user bestaat niet")
        #     user = User(username, "")
        #     # self.user_dict[username] = user
        #     # self.save_dict("user", self.user_dict)
        #     print("Welkom, " + username.title() + " , er is een account voor je aangemaakt!")
        # return user
        pass