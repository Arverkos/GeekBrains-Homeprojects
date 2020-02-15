class Road:
    __basic_mass = 25  # Атрибут, равный массе 1 м2 площади асфальта при его толщине в 1 см, 25 кг/(см*м2)

    def __init__(self, length_road, width_road, thickness_road):
        self._length = length_road  # Атрибут, длина участка дороги, м
        self._width = width_road  # Атрибут, ширина участка дороги, м
        self._thickness = thickness_road  # Атрибут, толщина асфальта на участке дороги, см

    def road_mass(self):
        mass = round(self._length * self._width *
                     self._thickness * self.__basic_mass / 1000, 2)  # Массу переводим в тонны
        print(f'Масса асфальта на участке составляет {mass} тонн')
        return mass


length_1 = int(input('Введите длинну участка (м): '))
width_1 = int(input('Введите ширину участка (м): '))
thickness_1 = int(input('Введите толщину асф. покрытия на участке (см): '))

road_1 = Road(length_1, width_1, thickness_1)

road_1.road_mass()
