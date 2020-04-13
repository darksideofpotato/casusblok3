from dal import Dal


class Program:
    def __init__(self):

        self.dal = Dal()

        self.username = input("Wat is je gebruikersnaam?")

        self.user_object = self.dal.login_user(self.username)

        self.menu()

    def menu(self):
        flag = True
        while flag:
            print(
                "Je bevind je in het menu. Wat wil je doen?\n\n"
                "Kies 'u' om naar de opties voor gebruikers te gaan\n"
                "Kies 'l' om naar de opties voor leveranciers te gaan\n"
                "Kies 'o' om naar de opties van orders te gaan\n"
                "Kies 'p' om naar de opties voor producten te gaan\n"
                "Kies 'lo' om uit te loggen \n"
                "Kies 'e' om af te sluiten\n"
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

            # region order options
            # TODO: Checken of alle menu dingen kloppen met de use cases
            if choice == 'o':
                print(
                    "Kies 'all' om alle orders te bekijken\n"
                    "Kies 'a' om een order handmatig te plaatsen\n"
                    "Kies 'c' om een order aan te passen\n"
                    
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
                elif choice == 'b':
                    # TODO: maken
                    pass
                elif choice == 'p':
                    # TODO: maken
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
                    "Kies 'a' om een product aan te passen\n"
                    "Kies 't' om een product toe te voegen\n"
                    "Kies 'd' om een product te verwijderen\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'a':
                    # TODO: maken
                    pass
                elif choice == 't':
                    # TODO: maken
                    pass
                elif choice == 'd':
                    # TODO: maken
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


Program()

