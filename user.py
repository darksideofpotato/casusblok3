import time

class User:
    def __init__(self, id, username, rol):
        self.userid = id
        self.username = username
        self.rol = rol

##### methods

    def get_info(self):
        print("Je bent ingelogd als " + self.username + " en hebt als rol " + self.rol)
        time.sleep(2)

    def get_user_id(self):
        return self.userid
