class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


thing_1 = Pencil('Карандаш')
thing_2 = Handle('Маркер')
thing_3 = Pen('Ручка')

thing_1.draw()
thing_2.draw()
thing_3.draw()
