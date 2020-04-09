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
    def database_disconnect(self, connection):
        if connection.is_connected():
            connection.close()
            print("Database is closed")

############################################ einde methods voor de databaseconnectie

##### User methods
    def login_user(self, username):
        connection = self.database_connect()

        sql = "SELECT * FROM gebruiker where gebruikersnaam like (%s)"

        data = (username,)
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()

        if result != []:

            print("Welkom, " + username.title())
            self.database_disconnect(connection)
            user = User(result[0][1], result[0][2])
            return user

        else:
            print("Deze user bestaat niet, of je hebt een typfout gemaakt. Probeer het nog een keer.")
            self.database_disconnect(connection)
            return False



