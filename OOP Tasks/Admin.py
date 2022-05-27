from User import User


class Admin(User):
    def __init__(self, first_name, last_name, age, email, login_attempts):
        super().__init__(first_name, last_name, age, email, login_attempts)
        self.priv = Privileges()
    pass


class Privileges():
    def __init__(self):
        self.privilegies = ["«Allowed to add message»", "«Allowed to delete users»", "«Allowed to ban users»"]

    def show_privileges(self):
        return self.privilegies
    pass


