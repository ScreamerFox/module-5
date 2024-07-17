

class House():                           # создаём класс
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Дом - {self.name}, в нём - {self.number_of_floors} этажей!'

    def __len__(self):
        return self.number_of_floors


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if not isinstance(value, int):
            print("Ошибка2")
        else:
            self.number_of_floors = self.number_of_floors + value
            return self
    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


house1 = House("Андреевский", 10)   # создаём 2 дома
house2 = House("Cleopatra", 20)


print(house1)
print(house2)

print(house1 == house2) # __eq__

house1 = house1 + 10 # __add__
print(house1)
print(house1 == house2)

house1 += 10 # __iadd__
print(house1)

house2 = 10 + house2 # __radd__
print(house2)

print(house1 > house2) # __gt__
print(house1 >= house2) # __ge__
print(house1 < house2) # __lt__
print(house1 <= house2) # __le__
print(house1 != house2) # __ne__







