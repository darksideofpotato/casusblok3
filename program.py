from dal import Dal

class Program:
    def __init__(self):
        self.dal = Dal()

        self.username = input("Wat is je gebruikersnaam?")

        self.user = self.dal.login_user(self.username)
        # Om te laten zien wat er in de file zit, print ik hier via de methode van dal al de namen die in de file staan.


Program()

