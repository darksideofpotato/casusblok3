import time

class User:
    def __init__(self, id, username, rol):
        self.userid = id
        self.username = username
        self.rol = rol

    # functie om de info van de ingelogde gebruiker te weergeven
    def get_info(self):
        print("Je bent ingelogd als " + self.username + " en hebt als rol " + self.rol)
        input("Druk op enter om terug naar het menu te gaan.")

    # functie om het huidige id van de ingelogde gebruiker te weergeven
    def get_user_id(self):
        return self.userid
