from time import sleep
import threading, random

#                        # Задача "Банковские операции"
class Bank():

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock  # класс в Python, который используется для обеспечения синхронизации между потоками

    def deposit(self):
        index = 0
        while index < 100:
            index += 1
            limit = random.randint(50, 500)  # Для генерации случайного целого числа
            self.balance += limit
            print(f"Пополнение: {limit}. Баланс: {self.balance}")
            try:
                if self.balance >= 500 and self.lock.locked() == True:
                    # self.lock.locked()
                    self.lock.release()         # метод разблокирующий поток
            except AttributeError:
                pass
            sleep(0.001)

    def take(self):
        index = 0
        while index < 100:
            index += 1
            limit = random.randint(50, 500)  # Для генерации случайного целого числа
            print(f"Запрос на {limit}")

            if limit <= self.balance:
                # self.lock.acquire(blocking=False)
                self.balance -= limit
                # self.lock.release()
                print(f"Снятие: {limit}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                try:
                    self.lock.acquire(blocking=False)        # метод блокирующий поток(и ждет очереди на блокировку)
                except AttributeError:
                    pass
            sleep(0.001)

bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()              # старт поток 1
th2.start()              #

th1.join()              # завершение потока 1
th2.join()              #

print(f'Итоговый баланс: {bk.balance}')

#_______________________________________________________
# def deposit():
#     balance = 0
#     index = 0
#     while index < 100:
#         index += 1
#         limit = random.randint(50, 500)
#         balance += limit
#         print(f"Пополнение: {limit}. Баланс: {balance}")
#
#     sleep(0.001)
##
#         # if balance >= 500: # and lock.locked() = True:
##
# rrrr = deposit()
# print(rrrr)

# def take():
#     balance = 1000
#     index = 0
#     while index < 100:
#         index += 1
#         limit = random.randint(50, 500)
#         if limit <= balance:
#             balance -= limit
#             sleep(0.001)
#             print(f"Снятие: {limit}. Баланс: {balance}")
#         else:
#             print(f"Запрос отклонён, недостаточно средств")
#             # self.lock.acquire(blocking=True)
# gbt = take()
# print(gbt)
# ------------------------------------------------
# import threading, random, time
#
# class Counter():
#
#     def __init__(self, start=0):
#         self.lock = threading.Lock()
#         self.value = start
#
#     def increment(self):
#         th_name = threading.current_thread().name
#         print(f'Th: {th_name} - ждет блокировку')
#         self.lock.acquire()
#         try:
#             print(f'Th: {th_name} - получил блокировку')
#             self.value = self.value + 1
#         finally:
#             self.lock.release()
#
#
# def worker(c):
#     for i in range(2):
#         pause = random.random()
#         th_name = threading.current_thread().name
#         print(f'Th: {th_name} - заснул на {pause:0.02f}')
#         time.sleep(pause)
#         c.increment()
#     print(f'Th: {th_name} - сделано.')
#
#
# counter = Counter()
# for i in range(2):
#     t = threading.Thread(target=worker, args=(counter,))
#     t.start()
#
# print('Ожидание рабочих потоков')
# main_thread = threading.main_thread()
# for t in threading.enumerate():
#     if t is not main_thread:
#         t.join()
# print(f'Счетчик: {counter.value}')
