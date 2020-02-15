class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} {self.colour} поехала')

    def stop(self):
        print(f'Машина {self.name} {self.colour} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} {self.colour} повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.colour} составляет {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость машины {self.name} {self.colour} составляет {self.speed}')
        else:
            print(f'Скорость машины {self.name} {self.colour} превышена на {self.speed - 60} - сбавьте скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость машины {self.name} {self.colour} составляет {self.speed}')
        else:
            print(f'Скорость машины {self.name} {self.colour} превышена на {self.speed - 40} - сбавьте скорость!')


class PoliceCar(Car):
    pass


car_1 = TownCar(50, 'Black', 'Kia', False)
car_2 = SportCar(150, 'Red', 'Ferrari', False)
car_3 = WorkCar(50, 'Yellow', 'Fiat', False)
car_4 = PoliceCar(80, 'White-Blue', 'Ford', True)

print(f' Машина {car_1.name} {car_1.colour} Скорость {car_1.speed} Полицейская? - {car_1.is_police}')
print(f' Машина {car_2.name} {car_2.colour} Скорость {car_2.speed} Полицейская? - {car_2.is_police}')
print(f' Машина {car_3.name} {car_3.colour} Скорость {car_3.speed} Полицейская? - {car_3.is_police}')
print(f' Машина {car_4.name} {car_4.colour} Скорость {car_4.speed} Полицейская? - {car_4.is_police}')

car_1.turn('Налево')
car_2.stop()
car_3.go()
car_4.show_speed()
car_3.show_speed()
