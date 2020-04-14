import mysql.connector
from mysql.connector import Error
from user import User
from company import Company
import datetime

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
            self.user = User(result[0][0], result[0][1], result[0][2])
            return self.user

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

        sql = "INSERT INTO leverancier (leveranciernaam, leverancieradres, " \
              "leverancieremail, levertijd) VALUES (%s, %s, %s, %s)"
        values = (naam, adres, email, levertijd)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

    def select_a_company(self, goal):
        connection = self.database_connect()

        sql = "SELECT leveranciernaam, leverancieradres, leverancieremail, levertijd FROM leverancier"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        print("De volgende leveranciers zitten in het systeem:")
        counter = 0
        for company in result:
            counter = counter + 1
            print(str(counter) + ". " + str(company))

        if goal == "action":
            chosen_company = int(input("Welke leverancier kies je? (nummer)"))
            chosen_company = - 1

            return (result[chosen_company][0])
        else:
            print("niet gelukt")
            pass

    def delete_company(self, chosen_company):
        connection = self.database_connect()

        sql = "DELETE FROM leverancier WHERE leveranciernaam = %s"
        value = (chosen_company,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted")

    def modify_company(self, chosen_company, new_name, new_adres, new_email, new_levertijd):
        connection = self.database_connect()

        sql = "UPDATE leverancier SET leveranciernaam = %s, leverancieradres = %s, " \
              "leverancieremail = %s, levertijd = %s WHERE leveranciernaam = %s"
        values = (new_name, new_adres, new_email, new_levertijd, chosen_company)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        print(cursor.rowcount, "record(s) affected")

#endregion

#region Order methods

    def select_an_order(self, goal):
        # TODO: string formatting en dergelijke
        connection = self.database_connect()

        sql = "SELECT orderID, datum, orderstatus, gebruikersnaam FROM `order` " \
              "JOIN gebruiker on `order`.gebruikerID = gebruiker.userID"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        print("De volgende orders zitten in het systeem:")
        counter = 0
        for order in result:
            counter = counter + 1
            print(str(counter) + ". " + str(order))

        # TODO: keuze kunnen maken tussen statussen van orders
        # TODO: laten zien van producten binnen een order
        # TODO: Bij delete alleen orders laten zien die in behandeling zijn

        if goal == "action":
            chosen_order = int(input("Welke order kies je? (nummer)"))
            chosen_order = chosen_order - 1

            return (result[chosen_order][0])
        else:
           pass


    def prepare_order(self):
        # TODO: netter maken
        userid = self.user.get_user_id()
        today_date = datetime.datetime.today()
        status = "In behandeling"

        connection = self.database_connect()

        sql = "INSERT INTO `order` (datum, orderstatus, gebruikerID) VALUES (%s, %s, %s)"

        values = (today_date, status, userid)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        new_order_id = cursor.lastrowid

        return new_order_id

    def place_order(self, order_id, product_id, quantity):
        # TODO: netter maken
        connection = self.database_connect()

        sql = "INSERT INTO `orderproduct` (orderID, productID, hoeveelheid) VALUES (%s, %s, %s)"

        values = (order_id, product_id, quantity)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

    def modify_order(self, order_id, what_to_change, new_value):
        connection = self.database_connect()
        # TODO: input check
        if what_to_change == "status":
            sql = "UPDATE `order` SET orderstatus = %s WHERE orderID = %s"
            values = (new_value, order_id)
        elif what_to_change == "hoeveelheid":
            sql = "UPDATE `orderproduct` SET hoeveelheid = %s WHERE orderID = %s and productID = %s"

            for order, product in order_id.items():
                values = (new_value, order, product)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        print(cursor.rowcount, "record(s) affected")

    def select_current_order_products(self, goal, orderID):
        # TODO: netter maken
        connection = self.database_connect()

        sql = "SELECT orderproduct.productID, productnaam, hoeveelheid FROM `orderproduct` " \
              "JOIN product on `product`.productID = orderproduct.productID WHERE orderID = %s"
        value = (orderID,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        result = cursor.fetchall()

        counter = 0
        for product in result:
            counter = counter + 1
            print(str(counter) + ". " + str(product))

        # TODO: een product aan kunnen passen
        if goal == "action":
            chosen_product = int(input("Welk product kies je? (nummer)"))
            chosen_product = chosen_product - 1

            chosen = {orderID: result[chosen_product][0]}
            return (chosen)
        else:
            pass

    def delete_order(self, chosen_order):
        self.delete_order_product(chosen_order, "null")
        # TODO: netter maken
        connection = self.database_connect()

        sql = "DELETE FROM `order` WHERE orderID = %s"
        value = (chosen_order,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted")

    def delete_order_product(self, order, product):
        #TODO: netter maken
        connection = self.database_connect()
        if product != "null":
            sql = "DELETE FROM orderproduct WHERE orderID = %s and productID = %s"
            value = (order, product,)
        else:
            sql = "DELETE FROM orderproduct WHERE orderID = %s"
            value = (order,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()
        print(cursor.rowcount, "record(s) deleted")
#endregion

#region Product methods
    def select_a_product(self, goal):
        # TODO: netter maken
        connection = self.database_connect()

        sql = "SELECT productID, productnaam, leveranciernaam, inkoopprijs, voorraadhoeveelheid, minimumvoorraad, maximumvoorraad FROM `product` " \
              "JOIN leverancier on `product`.leverancierID = leverancier.leverancierID"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        print("De volgende producten zitten in het systeem:")
        counter = 0
        # TODO: company aanpassen
        for company in result:
            counter = counter + 1
            print(str(counter) + ". " + str(company))

        if goal == "placeorder":

            list_of_items = {}
            flag = True
            while flag:
                chosen_product = input("Welke product kies je? (nummer)")
                print(chosen_product)

                if chosen_product != "":
                    chosen_product = int(chosen_product) - 1

                    hoeveelheid = input("Hoeveel stuks wil je bestellen?")
                    list_of_items[(result[chosen_product][0])] = hoeveelheid

                    print("item " + result[chosen_product][1] + " toegevoegd!")
                else:
                    flag = False
                    return list_of_items

        else:
           print("niet gelukt")
           pass
#endregion






