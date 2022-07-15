from abstract.utils import get_obj_or_404
from .serializers import Car_serializer
from .models import Car, Comment
from account.models import User

def create_car():
    body_types = ["седан", "купе", "хэтчбек", "минивен", "внедорожник", "пикап"]

    brand = input("Марка (без пробелов): ")
    model = input("Модель (без пробелов): ")
    year = int(input("Год выпуска: "))
    engine_volume = round(float(input("Объем двигателя: ")), 1)
    color = input("Цвет: ")

    print("Выберите тип кузова: ")
    for type in body_types:
        print(f"* {type}")
    body_t = input("==================================\nВыберите тип кузова: ")
    if body_t in body_types:
        body_type = body_t
    else:
        raise Exception("Такого типа не существует")

    mileage = int(input("Пробег: "))
    price = round(float(input("Цена: ")), 2)
    
    Car(brand, model, year, engine_volume, color, body_type, mileage, price)
    return "Продукт успешно создан"

def listing_cars():
    serializer = Car_serializer()
    cars = serializer.serialize_queryset()
    return cars

def retrieve_car(c_id):
    object = get_obj_or_404(Car, "id", int(c_id))
    return Car_serializer().serialize_obj(object)

def update_car(c_id):
    object = get_obj_or_404(Car, "id", int(c_id))
    field = input("Введите поле для изменения: ")
    if field in dir(object):
        value = input(f"{field} = ")
        setattr(object, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return retrieve_car(c_id)

def delete_car(c_id):
    object = get_obj_or_404(Car, "id", int(c_id))
    Car.objects.remove(object)
    return "Продукт успешно удален"

def create_comment():
    email = input("Введите email: ")
    user = get_obj_or_404(User, "email", email)
    print("Выберите марку и модель машины: ")
    for c in Car.objects:
        print(c)
    # В случае если есть объекты с одинаковой маркой, объект выбирается по модели
    brand_, model_ = input("===============================\n").split()
    car = get_obj_or_404(Car, "brand", brand_)
    if type(car) == list:
        for c in car:
            if c.model == model_:
                chosen_car = c
    else:
        chosen_car = car
    body = input("Введите комментарий: ")
    Comment(user, chosen_car, body)
    return "Комментарий успешно добавлен"

def like_car():
    email = input("Введите email: ")
    user = get_obj_or_404(User, "email", email)
    print("Выберите марку и модель машины: ")
    for c in Car.objects:
        print(c)
    # В случае если есть объекты с одинаковой маркой, объект выбирается по модели
    brand_, model_ = input("===============================\n").split()
    car = get_obj_or_404(Car, "brand", brand_)
    if type(car) == list:
        for c in car:
            if c.model == model_:
                chosen_car = c
    else:
        chosen_car = car
    chosen_car.likes += 1
    return "Лайк поставлен"

# Just for testing
u = User("admin", "admin")
u.register("12345678", "12345678")
u.login("12345678")

u1 = User("admin1", "admin1")
u1.register("123456789", "123456789")
u1.login("123456789")

u2 = User("admin2", "admin2")
u2.register("1234567890", "1234567890")
u2.login("1234567890")

Car("BMW", "M2", 2017, 3.0, "black", "купе", 0, 11.4567)
Car("BMW", "7", 2019, 2.0, "black", "седан", 0, 12.4567)
Car("Toyota", "Camry", 2020, 3.0, "black", "седан", 0, 13.4567)


