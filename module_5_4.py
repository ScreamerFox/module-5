
class House():                           # создаём класс
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name}, снесён, но он останется в истории!')


house1 = House("Андреевский", 10)   # создаём 2 дома
print(House.houses_history)
house2 = House("Cleopatra", 564)
print(House.houses_history)
house3 = House("Исаковский", 26)
print(House.houses_history)


del house1
del house3
print(House.houses_history)
