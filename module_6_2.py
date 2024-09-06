class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.__color = color
        self.owner = owner                   # владелец транспорта
        self.__model = model                # модель (марка) транспорта
        self.__engine_power = engine_power  # мощность двигателя
        # self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        # print(f'Модель:{self.__model}')
        return self.__model

    def get_horsepower(self):
        # print(f'Мощность двигателя: {self.__engine_power}')
        return self.__engine_power

    def get_color(self):
        # print(f'Цвет: {self.__color}')
        return self.__color

    def print_info(self):
        print(f'Модель: {self.get_model()}')
        print(f'Мощность двигателя: {self.get_horsepower()}')
        print(f'Цвет: {self.get_color()}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):  # Выбор цвета авто
        self.new_color = new_color

        if new_color.lower() not in Vehicle.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color}')

        else:
            self.__color = new_color
            # return Vehicle.__color

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5      # может поместиться только 5 пассажиров

#___________________________________
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()