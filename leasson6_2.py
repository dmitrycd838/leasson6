"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
   Значения данных атрибутов должны передаваться при создании экземпляра класса.
   Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
   необходимого для покрытия всего дорожного полотна. Использовать формулу:
   длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
   толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
"""

class Road:
    def __init__(self, width, lendth):
        self._width = width
        self._lendth = lendth

    @property
    def square(self):
        return self._lendth * self._width

    def get_weight_of_asphalt(self, weigt_ratio, thikness):
        asphalt = self.square * weigt_ratio * thikness
        return asphalt

my_road = Road(20, 5000)
print(my_road.get_weight_of_asphalt(25, 0.5))
