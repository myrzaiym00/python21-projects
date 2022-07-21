from .models import MyUser

def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    MyUser.create(username=username, password=password)
    return "Юзер успешно зарегистрирован"