
import runner_and_tournament as run_tur  # Импортируем файл "runner_and_tournament.py"
import runner
import unittest
import pytest
from functools import wraps
from _imp import is_frozen
from sympy.testing import pytest

# def indicator(func):
#     @wraps(func)    # обертка остовляет в себе имя декорируемой функции и ее документацию
#     def wrapper(*args, **kwargs):  # оболочка, предоставляет интерфейс для взаимодействия с компонентом или библиотекой
#         # print("Args:", args, kwargs)
#         # result = func(*args, **kwargs)
#         for i in args, kwargs:
#             for j in i:
#                 if j == getattr(RunnerTest.is_frozen, 'False', False): # функция, которая позволяет
#                 # if i == getattr(RunnerTest.is_frozen, 'False', False):
#                     # получать значение атрибута объекта, предоставляя его имя в виде строки
#                     unittest.SkipTest('Тесты в этом кейсе заморожены')
#                     # print(f'Вызов функции: {func.__name__}')
#         return func(*args, **kwargs)
#     return wrapper

# @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
class RunnerTest(unittest.TestCase):
    # global is_frozen
    is_frozen = False

    '''Создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого
    объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.'''

    # @indicator
    # @unittest.skip(is_frozen == True)#, 'Тесты в этом кейсе заморожены')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):

        sportsman = runner.Runner("Boris")
        for _ in range(10):
            sportsman.walk()
        self.assertEqual(sportsman.distance, 50)

    '''Далее вызовите метод run у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 100.'''

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        sportsman = runner.Runner("Fedot")
        for _ in range(10):
            sportsman.run()
        self.assertEqual(sportsman.distance, 100)

    '''Далее 10 раз у объектов вызываются методы run и walk соответственно.Т.к. дистанции должны
    быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.'''

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = runner.Runner("Boris")
        runner_2 = runner.Runner("Fedot")
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):    # Метод класса, вызываемый перед запуском тестов
        # global all_results
        cls.all_results = {}

    def setUp(self):

        self.sportsman_1 = run_tur.Runner('Усэйн ', 10)
        self.sportsman_2 = run_tur.Runner('Андрей', 9)
        self.sportsman_3 = run_tur.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values(): # получение значений из словаря
            to_print = {}
            for place, sportsman in result.items():
                to_print[place] = sportsman.name
            print(to_print)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_race(self):

        # создаем объект класса Соревнование
        self.compete = run_tur.Tournament(90, self.sportsman_1, self.sportsman_3)
        # Старт, и в словарь "all_result" записываем результат функции как (место:имя)
        all_results = self.compete.start()
        # имя последнего спортсмена
        self.last_runner = all_results[max(all_results.keys())].name
        self.assertTrue(self.last_runner == 'Ник')  # вызываем юнит-метод, сравниваем (True)
        TournamentTest.all_results[1] = all_results  # записываем словарь с ключом 1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_race(self):

        # создаем объект класса Соревнование
        self.compete = run_tur.Tournament(90, self.sportsman_2, self.sportsman_3)
        # Старт, и в словарь "all_result" записываем результат функции как (место:имя)
        all_results = self.compete.start()
        # имя последнего спортсмена
        self.last_runner = all_results[max(all_results.keys())].name
        self.assertTrue(self.last_runner == 'Ник')  # вызываем юнит-метод, сравниваем (True)
        TournamentTest.all_results[2] = all_results  # записываем словарь с ключом 2

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_race(self):

        # '''создаем объект класса Соревнование'''
        self.compete = run_tur.Tournament(90, self.sportsman_1, self.sportsman_2, self.sportsman_3)
        # Старт, и в словарь "all_result" записываем результат функции как (место:имя)
        all_results = self.compete.start()
        # имя последнего спортсмена
        self.last_runner = all_results[max(all_results.keys())].name
        self.assertTrue(self.last_runner == 'Ник')  # вызываем юнит-метод, сравниваем (True)
        TournamentTest.all_results[3] = all_results  # записываем словарь с ключом 3

if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2)
