class Animal:                    # Животные
    alive = True                 # живой
    fed = False                  # накормленный

    def __init__(self, name):
        self.name = name         # индивидуальное название каждого животного

    def eat(self, food):         # параметр, принимающий объекты классов растений
        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False

class Mammal(Animal):           # Млекопитающее
    pass

class Predator(Animal):         # Хищник
    pass


class Plant:                    # Растения
    edible = False              # съедобность

    def __init__(self, name):
        self.name = name        # индивидуальное название каждого растения

class Flower(Plant):           # Цветок
    def __init__(self, name):
         super().__init__(name)

class Fruit(Plant):             # Фрукт
    def __init__(self, name):
        super().__init__(name)
        self.edible = True         # Живой

#_________________________________________

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
