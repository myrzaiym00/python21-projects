from abstract import utils

class User:
    objects = []

    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.__password = None
        self.is_authenticated = False
        print(f"успешно создан пользователь {self.email}")
        User.objects.append(self)

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароли не совпадают")
        self.__password = password
        print(f"успешно зарегистрирован пользователь {self.email}")

    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_authenticated = True
        print(f"Пользователь {self.email} успешно зашел")

    def logout(self):
        utils.login_required(self)
        self.is_authenticated = False
        print(f"Пользователь {self.email} успешно вышел")

    def __str__(self):
        return self.email