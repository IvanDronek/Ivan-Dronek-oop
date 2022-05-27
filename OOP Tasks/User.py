class User:
    def __init__(self, first_name, last_name, age, email, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = login_attempts

    def describe_user(self):
        return f"Ви увійшли як {self.first_name} {self.last_name}"

    def greeting_user(self):
        return f"Вітаю ви повернулись {self.first_name}!"

    def increment_login_attempts(self):
        return self.login_attempts + 1

    @property
    def reset_login_attempts(self):
        login_attempts = 0
        return login_attempts
    pass


