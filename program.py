from dal import Dal
import time

class Program:
    # TODO: kijken of er meerdere classes gebruikt kunnen worden vanuit de dal class
    # TODO: automatisch orders plaatsen afwerken
    # TODO: de gebruiker altijd de optie geven om de applicatie af te sluiten

    def __init__(self):

        self.dal = Dal()

        self.username = input("Wat is je gebruikersnaam?")

        login = self.user_object = self.dal.login_user(self.username)

        # Checkt of de login goed of fout is gegaan.
        if login != False:
            self.menu()
        else:
            Program()

    def menu(self):
        flag = True
        while flag:
            # TODO: terug naar het desbetreffende menu geleid worden naar een actie,
            #  en niet altijd het algemene menu.

            print(
                "Je bevindt je in het menu. Wat wil je doen?\n\n"
                "Kies 'u' om naar de opties voor gebruikers te gaan\n"
                "Kies 'l' om naar de opties voor leveranciers te gaan\n"
                "Kies 'o' om naar de opties van orders te gaan\n"
                "Kies 'p' om naar de opties voor producten te gaan\n"
                "Kies 'lo' om uit te loggen \n"
                "Kies 'e' om af te sluiten\n"
                "Kies 'test' voor een demo van het automatische bevoorraadsysteem"
            )
            choice = input().lower()

            # region User options
            if choice == 'u':
                print(
                    "****Welkom in het overzichtmenu voor gebruikersgegevens.**** \n"
                    "Kies 'i' om je gebruikersinfo te bekijken.\n"
                    "Kies 'all' om een lijst van alle users te zien\n"
                    "Kies 'a' om een user toe te voegen\n"
                    "Kies 'd' om een user te verwijderen\n"
                    "Kies 'c' om een user aan te passen\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'i':
                    self.user_object.get_info()

                ## lijst van alle users kunnen bekijken
                elif choice == 'all':
                    self.dal.select_a_user('view')

                ## Het aamaken van een nieuwe gebruiker
                # TODO: dubbelen controleren alvorens de nieuwe user aan te maken
                elif choice == 'a':
                    if self.user_object.rol == "admin":
                        print("Je hebt ervoor gekozen om een nieuwe gebruiker aan te maken.")
                        flag2 = True
                        while flag2:
                            new_user_username = input ("Wat wordt de gebruikersnaam van de nieuwe gebruiker?")
                            if new_user_username == "" or new_user_username.isdigit():
                                print("Je input klopt niet helemaal, je hebt een lege "
                                      "waarde of getal ingevoerd. Probeer het nog een keer.")
                            else:
                                flag2 = False
                        new_user_role = input("Is het een admin(typ a) of employee(typ e)?")
                        if new_user_role == 'a':
                            new_user_role = 'admin'
                        elif new_user_role == 'e':
                            new_user_role = 'employee'

                        self.dal.add_user(new_user_username,new_user_role)

                        input("\nDe nieuwe user " + new_user_username + " is toegevoegd!\n "
                                "Druk op enter om terug naar het menu te gaan")
                        pass
                    else:
                        print("Je hebt niet de rechten om deze actie uit te voeren.")
                        pass

                ## Het verwijderen van een user
                elif choice == 'd':
                    print("Je hebt ervoor gekozen om een gebruiker te verwijderen.")
                    if self.user_object.rol == "admin":
                        selected_to_delete = self.dal.select_a_user('action')
                        confirm_delete = input("Je hebt gekozen om " + selected_to_delete + " te verwijderen. Weet je dit zeker? (y/n)")
                        if confirm_delete == "y":
                            self.dal.delete_user(selected_to_delete)
                            input("Je hebt met succes " + selected_to_delete + " verwijderd.\n"
                                "Druk op enter om terug naar het menu te gaan.")
                        else:
                            pass
                        pass
                    else:
                        print("Je hebt niet de rechten om deze actie uit te voeren.\n"
                              "Druk op enter om terug naar het menu te gaan.")
                        pass

                ## Het kiezen en aanpassen van een user
                elif choice == 'c':
                    print("Je hebt ervoor gekozen om de gegevens van een gebruiker aan te passen.")
                    if self.user_object.rol == "admin":
                        selected_to_change = self.dal.select_a_user('change')

                        new_user_username = input("Wat wordt de nieuwe gebruikersnaam? "
                                "\n(druk op enter om de huidige gebruikersnaam te behouden)")
                        if new_user_username == "" or new_user_username.isdigit():
                            print("De oude username " + selected_to_change.username + " wordt behouden")
                            new_user_username = selected_to_change.username

                        new_user_role = input("Is het een admin(a) of employee(e)?"
                            "\n(druk op enter om de huidige rol te behouden)")
                        if new_user_role == 'a':
                            new_user_role = 'admin'
                        elif new_user_role == 'e':
                            new_user_role = 'employee'
                        else:
                            print("Je hebt een foutieve waarde ingevoerd. Rol blijft onveranderd")
                            new_user_role = selected_to_change.rol

                        self.dal.modify_user(selected_to_change.userid, new_user_username, new_user_role)
                        input("De gegevens van " + new_user_username + " zijn succesvol aangepast. \n"
                                        "Druk op enter om terug naar het menu te gaan.")

                        pass
                    else:
                        print("Je hebt niet de rechten om deze actie uit te voeren."
                              "\n Druk op enter om terug naar het menu te gaan.")
                        pass

                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            # endregion

            # region Leverancier options
            elif choice == 'l':
                print(
                    "****Welkom in het overzichtmenu voor gebruikersgegevens.**** \n"
                    "Kies 'a' om een leverancier toe te voegen\n"
                    "Kies 'd' om een leverancier te verwijderen\n"
                    "Kies 'c' om een leverancier aan te passen\n"
                    "Kies 'all voor een volledige lijst van leveranciers\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'a':
                    print("Je hebt ervoor gekozen om een nieuwe leverancier aan te maken.")
                    flag2 = True
                    while flag2:
                        new_company_name = input("Wat is de naam van de leverancier?")
                        if new_company_name == "":
                            print("Je hebt een lege waarde ingevuld, probeer het nog een keer")
                        else:
                            flag2 = False
                    flag2 = True
                    while flag2:
                        new_company_adres = input("Wat is het adres van de leverancier?")
                        if new_company_adres == "" or new_company_adres.isdigit():
                            print("Je hebt een lege waarde of getal ingevuld, probeer het nog een keer")
                        else:
                            flag2 = False
                    flag2 = True
                    while flag2:
                        new_company_email = input("Wat is het emailadres van de leverancier?")
                        if new_company_email == "" or new_company_email.isdigit():
                            print("Je hebt een lege waarde of getal ingevuld, probeer het nog een keer")
                        else:
                            flag2 = False
                    flag2 = True
                    while flag2:
                        new_company_levertijd = input("Wat is de levertijd van de leverancier?")
                        if new_company_levertijd == "" or new_company_levertijd.isdigit():
                            print("Je hebt een lege waarde of getal ingevuld, probeer het nog een keer")
                        else:
                            flag2 = False

                    self.dal.add_company(new_company_name, new_company_adres, new_company_email, new_company_levertijd)

                    input("\nDe nieuwe leverancier " + new_company_name + " is toegevoegd!\n"
                        "Druk op enter om terug naar het menu te gaan.")
                    pass

                elif choice == 'd':
                    print("Je hebt ervoor gekozen om een leverancier te verwijderen.")
                    selected_to_delete = self.dal.select_a_company('action')
                    confirm_delete = input(
                        "Je hebt gekozen om " + selected_to_delete + " te verwijderen. Weet je dit zeker? (y/n)")
                    if confirm_delete == "y":
                        self.dal.delete_company(selected_to_delete)
                        input(selected_to_delete + " is verwijderd.\n"
                            "Druk op enter om terug naar het menu te gaan.")
                    else:
                        pass
                    pass

                elif choice == 'c':
                    print("Je hebt ervoor gekozen om een leverancier aan te passen.")
                    selected_to_change = self.dal.select_a_company('change')

                    new_company_name = input("Wat is de nieuwe naam van de leverancier? "
                                             "\n(druk op enter om de huidige naam te behouden)")
                    if new_company_name == "":
                        print("De leveranciernaam wordt niet aangepast.")
                        new_company_name = selected_to_change.leveranciernaam
                    new_company_adres = input("Wat is het adres van de leverancier?"
                                              "\n(druk op enter om het huidige adres te behouden)")
                    if new_company_adres == "" or new_company_adres.isdigit():
                        print("het adres wordt niet aangepast.")
                        new_company_adres = selected_to_change.leverancieradres
                    new_company_email = input("Wat is het emailadres van de leverancier?"
                                              "\n(druk op enter om het huidige email adres te behouden)")
                    if new_company_email == "" or new_company_email.isdigit():
                        print("Het email adres wordt niet aangepast.")
                        new_company_email = selected_to_change.leverancieremail
                    new_company_levertijd = input("Wat is de levertijd van de leverancier?"
                                                  "\n(druk op enter om de huidige levertijd te behouden)")
                    if new_company_levertijd == "" or new_company_levertijd.isdigit():
                        print("De levertijd van het bedrijf wordt niet aangepast.")
                        new_company_levertijd = selected_to_change.levertijd

                    self.dal.modify_company(selected_to_change.leverancierID, new_company_name, new_company_adres, new_company_email, new_company_levertijd)
                    input("De gegevens van " + new_company_name + " zijn succesvol aangepast.\n"
                                                                  "Druk op enter om terug naar het menu te gaan.")
                    pass

                elif choice == 'all':
                    self.dal.select_a_company('show')
                    input("Druk op enter om terug naar het menu te gaan.")
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            #endregion

            # region Order options
            elif choice == 'o':
                print(
                    "****Welkom in het overzichtmenu voor orders.**** \n"
                    "Kies 'all' om alle orders te bekijken\n"
                    "Kies 'a' om een order handmatig te plaatsen\n"
                    "Kies 'c' om een order aan te passen\n"
                    "Kies 'd' om een order te annuleren\n"                
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'all':
                    self.dal.select_an_order("view")
                    input("Druk op enter om terug naar het menu te gaan.")
                    pass
                if choice == 'a':
                    print("Je hebt ervoor gekozen om een order te plaatsen.\n"
                          "Kies eerst uit welke producten je wil bestellen.")
                    items_to_order = self.dal.select_a_product("placeorder")

                    new_order_id = self.dal.prepare_order()


                    for product, quantity in items_to_order.items():
                        self.dal.place_order(new_order_id, product, quantity)
                        whole_product = self.dal.get_product_by_id(product)
                        self.dal.modify_product(whole_product.productID,whole_product.leverancierID,
                                                whole_product.productnaam, whole_product.inkoopprijs,
                                                int(whole_product.voorraad) + int(quantity),
                                                whole_product.min,whole_product.max)


                    input("De bestelling is succesvol geplaatst! Druk op enter om door te gaan.")

                    pass
                elif choice == 'c':
                    ## Het aanpassen van de status
                    print("Je hebt gekozen om een order aan te passen.")
                    flag3 = True
                    while flag3:
                        try:
                            selected_to_change = self.dal.select_an_order('action')

                            what_to_change = ""
                            while what_to_change != "1" and what_to_change != "2":
                                what_to_change = input(str("""Wat wil je aanpassen aan deze order?
                                                                [1] Status
                                                                [2] Producten
                                                                > """))

                            if what_to_change == "1":
                                print("'1.' In behandeling\n"
                                      "'2.' Betaald\n"
                                      "'3.' Verzonden\n"
                                      "'4.' Geleverd")
                                flag2 = True
                                while flag2:
                                    new_order_status = input("Wat is de nieuwe status? (nummer)")

                                    if int(new_order_status) == 1:
                                        new_order_status = "In behandeling"
                                        flag2 = False
                                    elif int(new_order_status) == 2:
                                        new_order_status = "Betaald"
                                        flag2 = False
                                    elif int(new_order_status) == 3:
                                        new_order_status = "Verzonden"
                                        flag2 = False
                                    elif int(new_order_status) == 4:
                                        new_order_status = "Geleverd"
                                        flag2 = False
                                    else:
                                        print("Je invoer klopt niet, probeer het nog een keer")

                                self.dal.modify_order(selected_to_change, "status", new_order_status)
                                input("De nieuwe status is met succes aangepast. "
                                      "Druk op enter om terug naar het menu te gaan.")
                                flag3 = False

                            ## het aanpassen van de producten van een order
                            #TODO: optie om extra producten toe te voegen zolang order nog in behandeling is
                            elif what_to_change == "2":
                                print("Je hebt ervoor gekozen om de producten binnen de bestelling aan te passen.\n"
                                      "De volgende producten zitten binnen de order.")
                                chosen_product_and_order = self.dal.select_current_order_products("action", selected_to_change)

                                choice = input("Wat wil je met dit product doen?\n"
                                               "Kies 'v' om te verwijderen\n"
                                               "Kies 'h' om de hoeveelheid aan te passen")
                                if choice == "v":
                                    for order, product in chosen_product_and_order.items():
                                        self.dal.delete_order_product(order, product)
                                        input("Het product is succesvol uit het order verwijderd.\n"
                                              "Druk op enter om door te gaan.")
                                        flag3 = False
                                    pass
                                elif choice == "h":
                                    flag2 = True
                                    while flag2:
                                        #TODO: input check toevoegen op maximum te bestellen
                                        nieuwe_hoeveelheid = input("Naar welke hoeveelheid moet het aangepast worden?")
                                        if nieuwe_hoeveelheid == "" or nieuwe_hoeveelheid.isalpha():
                                            print("Je input is geen cijfer. Probeer het nog een keer.")
                                        else:
                                            self.dal.modify_order(chosen_product_and_order, "hoeveelheid", nieuwe_hoeveelheid)
                                            input("Het product is met succes aangepast. \\n"
                                                  "Druk op enter om terug naar het menu te gaan")
                                            flag2 = False
                                            flag3 = False
                                        pass
                                pass
                        except ValueError:
                            print("Je input klopt niet helemaal. Probeer het nog een keer.")
                            flag3 = True
                elif choice == 'd':
                    # TODO: Maken dat alleen bestellingen in behandeling verwijderd kunnen worden
                    chosen_order_to_delete = self.dal.select_an_order("action")

                    self.dal.delete_order(chosen_order_to_delete)
                    input("De order is succesvol verwijderd.\n"
                          "Druk op enter om door te gaan.")
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            #endregion

            #region Product options
            # TODO: Checken of alle menu dingen kloppen met de use cases
            elif choice == 'p':
                print(
                    "Kies 'all' om alle producten te bekijken\n"
                    "Kies 'a' om een product toe te voegen\n"
                    "Kies 'c' om een product aan te passen\n"
                    "Kies 'd' om een product te verwijderen\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'all':
                    self.dal.select_a_product("view")
                    pass
                elif choice == 'a':
                    new_product_name = input("Wat is de naam van het nieuwe product?")
                    while new_product_name == "":
                        new_product_name = input("Geen naam ingevoerd, probeer het opnieuw:")
                    print("Kies uit de lijst met leveranciers wie het product levert")

                    new_product_leverancier = self.dal.select_a_company("addproduct")

                    new_product_inkoopprijs = input("Wat is de inkoopprijs? (bijv 1.50)")
                    while float(new_product_inkoopprijs) <= 0 or new_product_inkoopprijs == \
                            "" or new_product_inkoopprijs.isalpha():
                        new_product_inkoopprijs = input("Je ingevoerde inkoopprijs "
                                                        "klopt niet helemaal. Probeer het nog een keer. ")

                    new_product_voorraad = 0

                    new_product_minvoorraad = input("Geef een limiet van de minimum voorraad")
                    while int(new_product_minvoorraad) < 0 or new_product_minvoorraad == \
                            "" or new_product_minvoorraad.isalpha():
                        new_product_minvoorraad = input("Je ingevoerde minimum klopt niet "
                                                        "helemaal. Probeer het nog een keer. ")

                    new_product_maxvoorraad = input("Geef een limiet van de maximum voorraad")
                    while int(new_product_maxvoorraad) < int(new_product_minvoorraad) or new_product_maxvoorraad == ""\
                            or new_product_maxvoorraad.isalpha():
                        new_product_maxvoorraad = input(f"Maximum voorraad kan niet kleiner zijn dan "
                                                        f"minimum voorraad ({new_product_minvoorraad}):,"
                                                        f"of je hebt een foute value ingevuld.")

                    self.dal.add_product(new_product_leverancier, new_product_name, new_product_inkoopprijs,
                                         new_product_voorraad, new_product_minvoorraad, new_product_maxvoorraad)

                    input("\nHet nieuwe product " + new_product_name + " is toegevoegd!"
                                                                       "Druk op enter om door te gaan.")
                    pass
                elif choice == 'c':
                    # TODO: beter maken
                    selected_to_change = self.dal.select_a_product('productaanpassen')
                    print(selected_to_change.productID)
                    #TODO: tekst over bedrijf aanpassen
                    leverancier = self.dal.select_a_company("action")
                    modified_values = selected_to_change.modify_product(leverancier)

                    for x in modified_values:
                        print(x)

                    self.dal.modify_product(int(selected_to_change.productID), int(modified_values[0]), str(modified_values[1]),
                                            float(modified_values[2]), int(modified_values[3]), int(modified_values[4]),
                                            int(modified_values[5]))
                    pass
                elif choice == 'd':
                    # TODO: netter maken
                    selected_to_delete = self.dal.select_a_product('action')
                    confirm_delete = input(
                        "Je hebt gekozen om " + str(selected_to_delete) + " te verwijderen. Weet je dit zeker? (y/n)")
                    if confirm_delete == "y":
                        self.dal.delete_product(selected_to_delete)
                    else:
                        pass
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            #endregion

            elif choice == 'lo':
                Program()
            elif choice == 'e':
                exit()

            ############# Test voor het automatisch bestellen van een product
            elif choice == 'test':
                self.dal.check_all_products()


Program()

