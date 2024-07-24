class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

house1 = House("Андреевский", 5)   # создаём 2 дома
house2 = House("Cleopatra", 10)
house1.go_to(11)
house2.go_to(2)
