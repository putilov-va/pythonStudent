from time import sleep
# from threading import Thread
import threading, random, queue
from queue import Queue

class Table:
    # global guest, number

    def __init__(self, number: int):
        self.number = number          # номер стола
        self.guest = None        # гость, который сидит за этим столом

class Guest(threading.Thread):
    # global name_guest

    def __init__(self, name_guest: str):
        self.name_guest = name_guest    # имя гостя
        super().__init__()

    def run(self):                          # время работы потока
        sleep(random.randint(3, 10))    # время застолья

class Cafe():

    # global name_guest, number, guests, tables, table

    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()      # очередь
        self.number = 1             # номер стола

    def guest_arrival(self, *guests):   # прибытие гостей
        self.guests = guests
        for guest in guests:
            for table in self.tables:
                if table.guest == None:   # Если есть свободный стол, то:
                    table.guest = guest     # то свободный стол гостю
                    guest.start()              # запускаем поток
                    print(f'{guest.name_guest} сел(-а) за стол номер {table.number}')
                    break           # стол найден, стоп цикл.
                                        # Если же свободных столов нет, то:
            if not guest.is_alive():        # проверяем отсутствие потока на текущий момент для гостя
                self.queue.put(guest)           # гостя добовляем в очередь
                print(f'{guest.name_guest} в очереди')

    def discuss_guests(self):       # обслужить гостей (каждому стол)
        while not self.queue.empty() or self.a_busy_tables():
            # Цикл: проверяем если гость в очереди, и освободился ли стол.
                # Переберём столы и определим занятые:
            busy_tables = [table for table in self.tables if table.guest != None]
            for table in busy_tables:   # перебор занятых столов.
                    # проверяем- если остановися поток на текущий момент для стола и гостя
                if not table.guest.is_alive():
                    print(f'{table.guest.name_guest} покушал(-а) и ушёл(ушла)')
                    table.guest = None           # присвоить - стол свободен
                    print(f'Стол номер {table.number} свободен')
                    if not self.queue.empty():       # проверка, что есть элементы в очереди (гости)
                        table.guest = self.queue.get()  # берём гостя из очереди
                        print(f'{table.guest.name_guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()             # старт обслуживания (потока)
            free_tables = [table for table in self.tables if table.guest == None] #
            for table in free_tables:       # перебор свободных столов.
                if not self.queue.empty():      # проверка, что есть элементы в очереди
                    table.guest = self.queue.get()  # берём гостя из очереди
                    print(f'{table.guest.name_guest} вышел(-ла) из очереди и сел(-а) за стол номер {self.number}')
                    table.guest.start()         # старт обслуживания (потока)

    def a_busy_tables(self):    # проверка стола на свободность
        busy = False
        for table in self.tables:
            if not table.guest == None:
                busy = True
                break
        return busy

# global name, number, guests, tables
table = Table
# Создание столов
tables = [Table(number) for number in range(1, 6)]    # столы в этом кафе (любая коллекция)
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Viktoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name_guest) for name_guest in guests_names]
# # Заполнение кафе столами
cafe = Cafe(*tables)
# # Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()
# table.guest.join()
# print(guests)
#_____________________________________________________
# класс Queue
# Clear() — очищает очередь;
# Contains(T item) — возвращает true, если элемент item имеется в очереди;
# Dequeue() — извлекает и возвращает первый элемент очереди;
# Enqueue(T item) — добавляет элемент в конец очереди;
# Peek() — возвращает первый элемент из начала очереди без его удаления.
#
# методы:
# Для добавления в очередь используйте метод put,
# для взятия - get.
# empty() — проверяет, есть ли в экземпляре Queue какие-либо элементы.
#  - Он возвращает True, если в очереди нет элементов. В противном случае
# возвращает False.
# #
# is_alive() — Для проверки выполнения потока в текущий момент
#
# Поскольку Queue является синхронизированным классом (не реентерабельным)
# при использовании несколькими потоками, даже если empty() возвращает True,
# нет гарантии, что операция put() будет заблокирована.
# Аналогично, не гарантируется, что get() не заблокируется даже после того,
# как метод empty() вернет False.

#_________________________________________________________________