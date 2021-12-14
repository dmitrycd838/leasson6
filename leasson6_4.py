"""
4. Реализуйте базовый класс Car.
  У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
  А также методы: go, stop, turn(direction), которые должны сообщать,
  что машина поехала, остановилась, повернула (куда).
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
  Для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Car:

    def __init__(self, speed, color, name, is_police,):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} начал(а) движение'

    def stop(self):
        return f'{self.name} остановился(ась)'

    def turn_right(self):
        return f'{self.name} повернул(а) направо'

    def turn_left(self):
        return f'{self.name} повернул(а) налево'

    def show_speed(self):
        return f'Текущая скорость {self.name}  {self.speed} км'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police,):
        super().__init__(speed, color, name, is_police,)

    def show_speed(self):
        print(f'Текущая скокрость городского автомобиля {self.name}  {self.speed} км')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police,):
        super().__init__(speed, color, name, is_police,)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police,):
        super().__init__(speed, color, name, is_police,)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed} км')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police,):
        super().__init__(speed, color, name, is_police,)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


BMW = SportCar(220, 'Синяя', 'BMW', False)
Volkswagen = TownCar(61, 'Черный', 'Volkswagen', False)
Hyundai = WorkCar(80, 'Белый', 'Hyundai', True)
Kia = PoliceCar(110, 'Розовая',  'Kia', True)
print(Hyundai.turn_left())
print(f'когда {Volkswagen.turn_right()}, тогда {BMW.stop()}')
print(f'{Hyundai.name}  {Hyundai.color}')
print(f'{BMW.name} это полицейский автомобиль? {BMW.is_police}')
print(f'{Kia.name} это полицейский автомобиль? {Kia.is_police}')
print(BMW.show_speed())
print(Volkswagen.show_speed())
print(Hyundai.show_speed())
print(Kia.show_speed())