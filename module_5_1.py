class House():                           # создаём класс
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # Доставляем на этаж
        if new_floor < 1:
            print("такого этажа не существует")
        elif new_floor > self.number_of_floors:
            print("такого этажа тоже не существует")
        else:
            print(f'Вы прибыли на {new_floor} этаж!')

house1 = House("Андреевский", 10)   # создаём 2 дома
house2 = House("Cleopatra", 521)

money1 = input('Здравствуйте, у вас больше 1000000$? да/нет: ')     # запрашиваем достаток клиента

def choice_house(money):                                            # Выбираем дом и этаж
    if money.lower() == 'да':
        lift2 = int(input('Добро пожаловать в элитный жк Cleopatra, на какой этаж хотите попасть?'))
        House.go_to(house2, lift2)
    else:
        lift = int(input('Добро пожаловать в жк Андреевский, на какой этаж хотите попасть?'))
        House.go_to(house1, lift)




choice_house(money1)
