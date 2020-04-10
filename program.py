from dal import Dal


class Program:
    def __init__(self):
        self.dal = Dal()

        self.username = input("Wat is je gebruikersnaam?")

        self.user_object = self.dal.login_user(self.username)

        self.menu()

    def menu(self):
        print("hoi")
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

            elif choice == 'l':
                print(
                    "Kies 'a' om een leverancier toe te voegen\n"
                    "Kies 'd' om een leverancier te verwijderen\n"
                    "Kies 'p' om een leverancier aan te passen\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'a':
                    pass
                elif choice == 'd':
                    pass
                elif choice == 'p':
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            if choice == 'o':
                print(
                    "Kies 'a' om een order aan te passen\n"
                    "Kies 'b' om de pending orders te bekijken\n"
                    "Kies 'p' om een order te plaatsen\n"
                    "Kies 'm' om terug naar het menu te gaan \n"
                    "Kies 'e' om af te sluiten\n"
                )
                choice = input()
                if choice == 'a':
                    pass
                elif choice == 'b':
                    pass
                elif choice == 'p':
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
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
                    pass
                elif choice == 't':
                    pass
                elif choice == 'd':
                    pass
                elif choice == 'm':
                    self.menu()
                elif choice == 'e':
                    exit()
                pass
            if choice == 'lo':
                Program()
            if choice == 'e':
                exit()


Program()

