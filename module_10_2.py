from time import sleep
from datetime import datetime
from threading import Thread

class Knight(Thread):

    def __init__(self, name, power, enemy=100):
        super().__init__()
        self.name = name        # имя рыцаря. (str)
        self.power = power      # сила рыцаря. (int)
        self.enemy = enemy

    def run(self):
        print(f"{self.name}, на нас напали!")
        # enemy = 100
        index = 1
        while index < self.power:
            sleep(1)                            # Задержка на 1 секунду
            self.enemy -= self.power            # сколько врагов осталось
            print(f"{self.name} сражается {index} день(дня), осталось {self.enemy} воинов.")
            if self.enemy != 0:
                index += 1
            else:
                print(f"{self.name} одержал победу спустя {index} дней(дня)!")
                break

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()
sleep(0.01)                          # Задержка на 0.01 секундуы
second_knight.start()
first_knight.join()
second_knight.join()
#_________________________________________________________
# name = 'Sir Lancelot'
# power = 20
# def bbrun():
#     print(f"{name}, на нас напали!")
#     enemy = 100
#     index = 1
#     while index < power:
#         sleep(1)                             # Задержка на 1 секунду
#         enemy -= power
#         print(f"{name} сражается {index} день(дня), осталось {enemy} воинов.")
#         if enemy != 0:
#             index += 1
#         else:
#             print(f"{name} одержал победу спустя {index} дней(дня)!")
#             break
# bbrun()