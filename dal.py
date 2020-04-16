import mysql.connector
from mysql.connector import Error
from user import User
from company import Company
from product import Product
from product_handler import Producthandler
import datetime
from admin import Admin
from employee import Employee

global connection

class Dal:

# region Database

    # Het openen van een databaseconnectie
    @staticmethod
    def database_connect():
            connection = mysql.connector.connect(
              host="localhost",
              database='casus_voorraden',
              user="root",
              passwd="root", auth_plugin='mysql_native_password'
            )

            return connection

    # Het sluiten van een databaseconnectie als die open staat
    def database_disconnect(self, connection):
        if connection.is_connected():
            connection.close()

#endregion

#region User methods

    # De login functie. Logt in op basis van de gebruikersnaam, en maakt op basis van de rol een object
    # van admin of employee aan.
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

            if result[0][2] == 'admin':
                self.user = Admin(result[0][0], result[0][1], result[0][2])
            elif result[0][2] == 'employee':
                self.user = Employee(result[0][0], result[0][1], result[0][2])

            self.database_disconnect(connection)
            return self.user

        # Als een user niet in de database voorkomt, wordt een errormessage gegevens en kan de gebruiker nogmaals
        # proberen in te loggen
        else:
            print("Deze user bestaat niet, of je hebt een typfout gemaakt. Probeer het nog een keer.")
            self.database_disconnect(connection)
            return False

    # Functie om een user toe te voegen. Gebruikt de gegevens die in het menu worden ingevuld.
    def add_user(self, username, role):
        connection = self.database_connect()

        sql = "INSERT INTO gebruiker (gebruikersnaam, rol) VALUES (%s, %s)"
        values = (username, role)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        self.database_disconnect(connection)

    # Via deze functie kunnen alle users worden weergeven, en indien nodig kan er ook een uitgekozen worden voor
    # een bewerking (modify of delete)
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
            chosen_user = chosen_user - 1

            return (result[chosen_user][0])

        self.database_disconnect(connection)

    # Een user kan worden gedelete via dezee functie
    def delete_user(self, chosen_user_username):
        connection = self.database_connect()

        sql = "DELETE FROM gebruiker WHERE gebruikersnaam = %s"
        value = (chosen_user_username,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()

        self.database_disconnect(connection)

    # De gegevens van een user worden via de functie aangepast
    # TODO: doen via user class zodat niet alle gegevens opnieuw ingevuld hoeven te worden
    def modify_user(self, chosen_user, new_username, new_role):
        connection = self.database_connect()

        sql = "UPDATE gebruiker SET gebruikersnaam = %s, rol = %s WHERE gebruikersnaam = %s"
        values = (new_username, new_role, chosen_user)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        self.database_disconnect(connection)

#endregion

#region Company methods

    # De functie om een nieuwe leverancier toe te voegen. De waardes worden meegegeven vanuit het menu
    def add_company(self, naam, adres, email, levertijd):
        connection = self.database_connect()

        sql = "INSERT INTO leverancier (leveranciernaam, leverancieradres, " \
              "leverancieremail, levertijd) VALUES (%s, %s, %s, %s)"
        values = (naam, adres, email, levertijd)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        self.database_disconnect(connection)

    # De functie om alle leveranciers te weergeven, en om een leverancier uit te kiezen, om bijvoorbeeld
    # te verwijderen of om de gegevens van aan te passen. Er wordt gebruikt van de parameter 'goal' om dit
    # verschil aan te geven.
    def select_a_company(self, goal):
        connection = self.database_connect()

        sql = "SELECT leverancierID, leveranciernaam, leverancieradres, leverancieremail, levertijd FROM leverancier"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        print("De volgende leveranciers zitten in het systeem:")
        counter = 0
        for company in result:
            counter = counter + 1
            print(str(counter) + ". " + str(company))

        if goal == "action":
            try:
                chosen_company = int(input("Welke leverancier kies je? (nummer)"))
                chosen_company = chosen_company - 1

                return (result[chosen_company][0])
            except ValueError:

                return ""
        else:
            print("niet gelukt")
            pass

        self.database_disconnect(connection)

    # Functie om een leverancier te verwijderen
    def delete_company(self, chosen_company):
        connection = self.database_connect()

        sql = "DELETE FROM leverancier WHERE leveranciernaam = %s"
        value = (chosen_company,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()

        self.database_disconnect(connection)

    # Functie om de gegevens van een leverancier aan te passen
    # TODO: doen via leverancier class zodat niet alle gegevens opnieuw ingevuld hoeven te worden
    def modify_company(self, chosen_company, new_name, new_adres, new_email, new_levertijd):
        connection = self.database_connect()

        sql = "UPDATE leverancier SET leveranciernaam = %s, leverancieradres = %s, " \
              "leverancieremail = %s, levertijd = %s WHERE leveranciernaam = %s"
        values = (new_name, new_adres, new_email, new_levertijd, chosen_company)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        self.database_disconnect(connection)

    # Een functie specifiek om het ID van een leverancier op te vragen, op basis van een productID.
    def get_company_id_from_product(self, product):
        connection = self.database_connect()

        sql_leverancier = "SELECT leverancierID FROM product WHERE productID = %s"

        cursor = connection.cursor()
        value = (product,)
        cursor.execute(sql_leverancier, value)
        result2 = cursor.fetchall()

        self.database_disconnect(connection)
        return result2

#endregion

#region Order methods

    # Functie om alle orders te kunnen laten zien, en om een order uit te kiezen (om aan te passen of te annuleren)
    # TODO: orderproducten weergeven (functie staat iets naar beneden)
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
            print(str(counter) + ". ", end= " ")
            for x in order:
                x = '{:20}'.format(str(x))
                print(x, end= " ")
            print("\n")



        # TODO: keuze kunnen maken tussen statussen van orders
        # TODO: Bij delete alleen orders laten zien die in behandeling zijn

        if goal == "action":
            chosen_order = int(input("Welke order kies je? (nummer)"))
            chosen_order = chosen_order - 1

            return (result[chosen_order][0])
        else:
           pass

        self.database_disconnect(connection)

    # Functie die een order zelf aanmaakt. Deze functie is een voorbereiding op het aanmaken van
    # de orderproducten. Daarom wordt de orderID gereturned.
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

        self.database_disconnect(connection)
        return new_order_id

    # Binnen deze functie wordt voor het aanmaken van een order het orderproduct ingevuld.
    # Dit op basis van het orderID van de vorige functie, en de productID's die uitgekozen zijn.
    def place_order(self, order_id, product_id, quantity):
        # TODO: netter maken
        connection = self.database_connect()

        sql = "INSERT INTO `orderproduct` (orderID, productID, hoeveelheid) VALUES (%s, %s, %s)"

        values = (order_id, product_id, quantity)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()


        self.database_disconnect(connection)

    # Functie om een order aan te passen
    # TODO: doen via classes zodat niet alle gegevens opnieuw ingevuld hoeven te worden
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

        self.database_disconnect(connection)

    # Functie om een orderproduct te selecteren op basis van een orderID
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

        self.database_disconnect(connection)

    # Functie om een order te verwijderen
    def delete_order(self, chosen_order):
        self.delete_order_product(chosen_order, "null")
        # TODO: netter maken
        connection = self.database_connect()

        sql = "DELETE FROM `order` WHERE orderID = %s"
        value = (chosen_order,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()

        self.database_disconnect(connection)

    # Wanneer een order wordt verwijderd, worden via deze functie ook automatisch de orderproducten verwijderd.
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

        self.database_disconnect(connection)
#endregion

#region Product methods
############################################ Hier zijn de functies aangepast op de classes, zoals besproken ###############################
    def select_a_product(self, goal):
        # TODO: netter maken
        # TODO: weergave inkoopprijs
        connection = self.database_connect()

        sql = "SELECT productID, productnaam, leveranciernaam, inkoopprijs, voorraadhoeveelheid, minimumvoorraad, maximumvoorraad FROM `product` " \
           "JOIN leverancier on `product`.leverancierID = leverancier.leverancierID"

        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        product_handler = Producthandler(result)

        picked_product = product_handler.select_a_product(goal)

        if goal == "productaanpassen":
            result2 = self.get_company_id_from_product(picked_product[0])
            products_to_change = product_handler.product_aanpassen_handler(result2, picked_product)
            self.database_disconnect(connection)
            return products_to_change
        else:
            self.database_disconnect(connection)
            return picked_product

    def add_product(self, leverancier, productnaam, inkoopprijs, voorraad, min, max):
        connection = self.database_connect()

        sql = "INSERT INTO product (leverancierID, productnaam, inkoopprijs, " \
              "voorraadhoeveelheid, minimumvoorraad, maximumvoorraad) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (leverancier, productnaam, inkoopprijs, voorraad, min, max)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        self.database_disconnect(connection)

    def delete_product(self, chosen_product):
        # Er is voor gekozen om de koppelingen uit andere tabellen niet te verwijderen. Dit omdat er nog
        # orders kunnen lopen, en het bedrijf deze appart wil cancelen indien nodig. Ook kan het het geval zijn
        # dat een product eerst opgemaakt wordt (inclusief wat er nog besteld is) en dat het product
        # vervolgens pas ge "discontinued" wordt.

        connection = self.database_connect()

        sql = "DELETE FROM product WHERE productID = %s"
        value = (chosen_product,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        connection.commit()
        self.database_disconnect(connection)

    def modify_product(self, chosen_product, leverancier, naam, prijs, voorraad, min, max):
        connection = self.database_connect()

        sql = "UPDATE product SET leverancierID = %s, productnaam = %s, inkoopprijs = %s, " \
              "voorraadhoeveelheid = %s, minimumvoorraad = %s, maximumvoorraad = %s WHERE productID = %s"

        values = (leverancier, naam, prijs, voorraad, min, max, chosen_product)
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        self.database_disconnect(connection)

    def check_all_products(self):
        # Deze functie controleerd alle producten in de database of er iets nieuws bijbesteld moet worden.
        # Is dit het geval, dan zal een product bijbesteld worden.

        connection = self.database_connect()

        sql = "SELECT productID, productnaam, leverancierID, inkoopprijs, voorraadhoeveelheid, minimumvoorraad, maximumvoorraad FROM `product` "

        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        counter = 1
        for product in result:
            the_product = Product(product[0], product[1], product[2], product[3], product[4], product[5], product[6])
            outcome_check = the_product.check_quantity()

            if outcome_check != None:
                #TODO: zorgen dat bij meerdere producten van een leverancier in een keer niet meerdere order
                # ID's worden gemaakt

                print("daar moeten " + str(outcome_check) + " van worden bijbesteld")
                new_order_id = self.prepare_order()
                self.place_order(new_order_id, product[0], outcome_check)
                self.modify_product(product[0], new_order_id, product[2], product[3], product[6], product[5], product[6])
                pass
            else:
                counter = counter + 1
        pass
        self.database_disconnect(connection)

    def get_product_by_id(self, id):
        connection = self.database_connect()

        sql = "SELECT * FROM product WHERE productID = %s"
        value = (id,)
        cursor = connection.cursor()
        cursor.execute(sql, value)
        result = cursor.fetchall()

        got_product = Product(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4],
                              result[0][5], result[0][6])

        self.database_disconnect(connection)
        return got_product
#endregion






