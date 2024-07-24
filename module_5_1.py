class House():                           # создаём класс
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # Доставляем на этаж
        for i in range(1, new_floor + 1):
            if new_floor < 1:
                print("такого этажа не существует")
                break
            elif new_floor > self.number_of_floors:
                print("такого этажа тоже не существует")
                break
            else:
                print(f'Вы прибыли на {i} этаж!')

house1 = House("Андреевский", 10)   # создаём 2 дома
house2 = House("Cleopatra", 2)
house1.go_to(11)
house2.go_to(2)
