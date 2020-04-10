class User:
    def __init__(self, id, username, rol):
        self.userid = id
        self.username = username
        self.rol = rol

##### methods

    def get_info(self):
        print(self.username, self.rol)
    #method om een product te bestellen
    def order_product(self):
        pass

    #method om een bedrijf toe te voegen
    def add_company(self):
        pass

    #method om een user te deleten
    def delete_user(self):
        pass

    #method om uit te loggen
    def logout(self):
        pass