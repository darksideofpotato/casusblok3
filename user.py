class User:
    def __init__(self, id, username, rol):
        self.userid = id
        self.username = username
        self.rol = rol

##### methods

    def get_info(self):
        print(self.username, self.rol)

    def get_user_id(self):
        return self.userid

    #method om een product te bestellen
    def order_product(self):
        pass