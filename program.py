from dal import Dal


class Program:
    # TODO: rollen toevoegen
    # TODO: kijken of er meerdere classes gebruikt kunnen worden vanuit de dal class
    # TODO: automatisch orders plaatsen afwerken

    def __init__(self):

        self.dal = Dal()

        self.username = input("Wat is je gebruikersnaam?")

        self.user_object = self.dal.login_user(self.username)

        self.menu()

    def menu(self):
        flag = True
        while flag:
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
            # TODO: Security er dergelijke kloppend maken
            # Verder klaar!
            if choice == 'u':
                print(
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
                elif choice == 'a':
                    new_user_username = input ("Wat wordt de username van de nieuwe user?")
                    new_user_role = input("Is het een admin(a) of employee(e)?")
                    if new_user_role == 'a':
                        new_user_role = 'admin'
                    elif new_user_role == 'e':
                        new_user_role = 'employee'

                    self.dal.add_user(new_user_username,new_user_role)

                    print("\nDe nieuwe user " + new_user_username + " is toegevoegd!")
                    pass

                ## Het verwijderen van een user
                elif choice == 'd':
                    selected_to_delete = self.dal.select_a_user('action')
                    confirm_delete = input("Je hebt gekozen om " + selected_to_delete + " te verwijderen. Weet je dit zeker? (y/n)")
                    if confirm_delete == "y":
                        self.dal.delete_user(selected_to_delete)
                    else:
                        pass
                    pass

                ## Het kiezen en aanpassen van een user
                elif choice == 'c':
                    selected_to_change = self.dal.select_a_user('action')

                    new_user_username = input("Wat wordt de nieuwe username?")
                    new_user_role = input("Is het een admin(a) of employee(e)?")
                    if new_user_role == 'a':
                        new_user_role = 'admin'
                    elif new_user_role == 'e':
                        new_user_role = 'employee'

                    self.dal.modify_user(selected_to_change, new_user_username, new_user_role)

                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            # endregion

            # region Leverancier options
            # TODO: Checken of alle menu dingen kloppen met de use cases
            elif choice == 'l':
                print(
                    "Kies 'a' om een leverancier toe te voegen\n"
                    "Kies 'd' om een leverancier te verwijderen\n"
                    "Kies 'c' om een leverancier aan te passen\n"
                    "Kies 'all voor een volledige lijst van leveranciers\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'a':
                    new_company_name = input("Wat is de naam van de leverancier?")
                    new_company_adres = input("Wat is het adres van de leverancier?")
                    new_company_email = input("Wat is het emailadres van de leverancier?")
                    new_company_levertijd = input("Wat is de levertijd van de leverancier?")

                    self.dal.add_company(new_company_name, new_company_adres, new_company_email, new_company_levertijd)

                    print("\nDe nieuwe leverancier " + new_company_name + " is toegevoegd!")
                    pass
                elif choice == 'd':
                    selected_to_delete = self.dal.select_a_company('action')
                    confirm_delete = input(
                        "Je hebt gekozen om " + selected_to_delete + " te verwijderen. Weet je dit zeker? (y/n)")
                    if confirm_delete == "y":
                        self.dal.delete_company(selected_to_delete)
                    else:
                        pass
                    pass
                elif choice == 'c':
                    # TODO: beter maken
                    selected_to_change = self.dal.select_a_company('action')

                    new_company_name = input("Wat is de naam van de leverancier?")
                    new_company_adres = input("Wat is het adres van de leverancier?")
                    new_company_email = input("Wat is het emailadres van de leverancier?")
                    new_company_levertijd = input("Wat is de levertijd van de leverancier?")


                    self.dal.modify_company(selected_to_change, new_company_name, new_company_adres, new_company_email, new_company_levertijd)
                    pass
                elif choice == 'all':
                    self.dal.select_a_company('show')
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            #endregion

            # region Order options
            # TODO: Checken of alle menu dingen kloppen met de use cases
            if choice == 'o':
                print(
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
                    pass
                if choice == 'a':
                    items_to_order = self.dal.select_a_product("placeorder")

                    print(items_to_order)

                    new_order_id = self.dal.prepare_order()

                    for product, quantity in items_to_order.items():
                        self.dal.place_order(new_order_id, product, quantity)

                    pass
                elif choice == 'c':
                    ## Het aanpassen van de status
                    selected_to_change = self.dal.select_an_order('action')

                    what_to_change = input("Wat wil je aanpassen aan deze order?")
                    #TODO: Toevoegen welke keuzes je hebt

                    if what_to_change == "status":
                        print("'1.' In behandeling\n"
                              "'2.' Betaald\n"
                              "'3.' Verzonden\n"
                              "'4.' Geleverd")
                        flag2 = True
                        while flag2:
                            new_order_status = input("Wat is de nieuwe status?")

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

                    ## het aanpassen van de producten van een order
                    #TODO: optie om extra producten toe te voegen zolang order nog in behandeling is
                    elif what_to_change == "producten":
                        chosen_product_and_order = self.dal.select_current_order_products("action", selected_to_change)
                        #TODO: print bijzetten
                        choice = input("Wat wil je met dit product doen?")
                        if choice == "verwijderen":
                            for order, product in chosen_product_and_order.items():
                                self.dal.delete_order_product(order, product)
                            pass
                        elif choice == "hoeveelheid":
                            #TODO: input check toevoegen
                            #TODO: netter maken
                            nieuwe_hoeveelheid = input("Naar welke hoeveelheid moet het aangepast worden?")
                            self.dal.modify_order(chosen_product_and_order, "hoeveelheid", nieuwe_hoeveelheid)
                            pass
                        pass

                    else:
                        print("Je input klopt niet helemaal, probeer het nog een keer.")
                        # TODO: toevoegen flag loop voor de else

                        pass
                elif choice == 'd':
                    # TODO: Maken dat alleen bestellingen in behandeling verwijderd kunnen worden
                    chosen_order_to_delete = self.dal.select_an_order("action")

                    self.dal.delete_order(chosen_order_to_delete)
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            #endregion

            #region Product options
            # TODO: Checken of alle menu dingen kloppen met de use cases
            if choice == 'p':
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
                    #TODO: input checks
                    new_product_name = input("Wat is de naam van het nieuwe product?")
                    new_product_leverancier = self.dal.select_a_company("action")
                    new_product_inkoopprijs = input("Wat is de inkoopprijs?")
                    new_product_voorraad = 0
                    new_product_minvoorraad = input("Geef een limiet van de minimum voorraad")
                    new_product_maxvoorraad = input("Geef een limiet van de maximum voorraad")

                    self.dal.add_product(new_product_leverancier, new_product_name, new_product_inkoopprijs,
                                         new_product_voorraad, new_product_minvoorraad, new_product_maxvoorraad)

                    print("\nHet nieuwe product " + new_product_name + " is toegevoegd!")
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

            if choice == 'lo':
                Program()
            if choice == 'e':
                exit()

            ############# Test voor het automatisch bestellen van een product
            elif choice == 'test':
                self.dal.check_all_products()


Program()

