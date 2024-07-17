class House():                           # создаём класс
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Дом - {self.name}, в нём - {self.number_of_floors} этажей!'

house1 = House("Андреевский", 10)   # создаём 2 дома
house2 = House("Cleopatra", 521)



print(house1)
print(house2)
print(len(house1))
print(len(house2))
