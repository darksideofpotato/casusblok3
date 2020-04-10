import mysql.connector
from mysql.connector import Error
from user import User

global connection

class Dal:

#region Database
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
#endregion

#region User methods


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
            user = User(result[0][0], result[0][1], result[0][2])
            return user

        else:
            print("Deze user bestaat niet, of je hebt een typfout gemaakt. Probeer het nog een keer.")
            self.database_disconnect(connection)
            return False


    def add_user(self, username, role):
        connection = self.database_connect()

        sql = "INSERT INTO gebruiker (gebruikersnaam, rol) VALUES (%s, %s)"
        values = (username, role)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()


    def select_a_user(self, goal):
        connection = self.database_connect()

        sql = "SELECT gebruikersnaam, rol FROM gebruiker"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        print("De volgende users zitten in het systeem:")
        counter = 0
        for user in result:
            counter = counter + 1
            print(str(counter) + ". " + str(user))

        if goal == "action":
            chosen_user = int(input("Welke user kies je? (nummer)"))
            chosen_user = - 1

            return (result[chosen_user][0])
        else:
            print("niet gelukt")
            pass


    def delete_user(self, chosen_user_username):
        connection = self.database_connect()

        sql = "DELETE FROM gebruiker WHERE gebruikersnaam = %s"
        value = (chosen_user_username,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted")


    def modify_user(self, chosen_user, new_username, new_role):
        connection = self.database_connect()

        sql = "UPDATE gebruiker SET gebruikersnaam = %s, rol = %s WHERE gebruikersnaam = %s"
        values = (new_username, new_role, chosen_user)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        print(cursor.rowcount, "record(s) affected")

#endregion

#region Company methods
    def add_company(self, naam, adres, email, levertijd):
        connection = self.database_connect()

        sql = "INSERT INTO leverancier (leveranciernaam, leverancieradres, leverancieremail, levertijd) VALUES (%s, %s, %s, %s)"
        values = (naam, adres, email, levertijd)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()


#endregion






