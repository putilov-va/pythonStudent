class House:
    "Этажность застройки"

    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors
        # self.h1 = ()
        # self.h2 = ()

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"Такого этажа не существует")
            # break
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __len__(self):
        return self.number_of_floors


    def __eq__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, (int, House)):
            return int(self.number_of_floors) > int(other.number_of_floors)

    def __le__(self, other):
        if isinstance(other, (int, House)):
            return int(self.number_of_floors) <= int(other.number_of_floors)

    def __ge__(self, other):
        if isinstance(other, (int, House)):
            return int(self.number_of_floors) >= int(other.number_of_floors)

    def __ne__(self, other):
        if isinstance(other, (int, House)):
            return int(self.number_of_floors) != int(other.number_of_floors)

    def __add__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError("Правый оператор должен быть int")
        floors_ = other if isinstance(other, int) else other.number_of_floors
        return House(self.name, self.number_of_floors + floors_)

    def __iadd__(self, other):
        # if not isinstance(other, (int, House)):
        #     raise ArithmeticError("Правый оператор должен быть int или объектом House")
        floors_ = other if isinstance(other, int) else other.number_of_floors
        self.number_of_floors += floors_
        return House(self.name, self.number_of_floors)

    def __radd__(self, other):
        return self + other

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
