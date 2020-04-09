from dal import Dal

class Program:
    def __init__(self):
        self.dal = Dal()

        flag = True
        while flag:
            self.username = input("Wat is je gebruikersnaam?")

            if self.dal.login_user(self.username) == True:
                flag = False

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
            # "Kies 'lo' om uit te loggen \n"
            # "Kies 'exit' om af te sluiten\n"
            )
            choice = input()

            if choice == 'u':
                # "Kies 'u' om je gebruikersinfo te bekijken.\n"
                # "Kies 'au' om een user toe te voegen\n"
                # "Kies 'du' om een user te verwijderen\n"
                # "Kies 'lo' om uit te loggen \n"
                # "Kies 'exit' om af te sluiten\n"
                pass
            if choice == 'l':
                # "Kies 'ac' om een leverancier toe te voegen\n"
                # "Kies 'dc' om een leverancier te verwijderen\n"
                # "Kies 'lo' om uit te loggen \n"
                # "Kies 'exit' om af te sluiten\n"
                pass
            if choice == 'o':
                # "Kies 'oa' om een order aan te passen\n"
                # "Kies 'po' om de pending orders te bekijken\n"
                # "Kies 'op' om een order te plaatsen\n"
                # "Kies 'lo' om uit te loggen \n"
                # "Kies 'exit' om af te sluiten\n"
                pass
            if choice == 'p':
                # "Kies 'pa' om een product aan te passen\n"
                # "Kies 'lo' om uit te loggen \n"
                # "Kies 'exit' om af te sluiten\n"
                pass

















Program()

