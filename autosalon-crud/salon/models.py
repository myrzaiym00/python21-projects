from abstract import utils

class Car:
    objects = []
    id_ = 0

    def __init__(self, brand, model, year, engine_volume, color, body_type, mileage, price):
        self.id = Car.id_
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = price
        self.likes = 0

        Car.objects.append(self)
        Car.id_ += 1

    def __str__(self):
        return f"{self.brand} {self.model}"

    @property
    def comments(self):
        return [c for c in Comment.objects if c.car == self]

class Comment:
    objects = []

    def __init__(self, user, car, body):
        utils.login_required(user)
        from datetime import datetime
        self.user = user
        self.car = car
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)
    
    def __str__(self):
        return f"{self.user.email} - [{self.created_at}] - {self.body}"