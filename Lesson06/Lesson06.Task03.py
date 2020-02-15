class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage,
                        'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f' Полное имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + (self._income['bonus'])
        print(f'Доход {self.name} {self.surname} с учетом премии {total_income} рублей')


person_1 = Position('Petr', 'Petrov', 'Intern', 20000, 0)
person_2 = Position('Vasiliy', 'Pupkin', 'СEO', 300000, 200000)

# print(worker_1.name)
# print(worker_1.surname)
# print(worker_1.position)
person_1.get_full_name()
person_1.get_total_income()
person_2.get_full_name()
person_2.get_total_income()
