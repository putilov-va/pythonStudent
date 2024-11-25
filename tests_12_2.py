import runner_and_tournament as run_tur  # Импортируем файл "runner_and_tournament.py"
import unittest

class TournamentTest(unittest.TestCase):

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

    def test_first_race(self):

        # создаем объект класса Соревнование
        self.compete = run_tur.Tournament(90, self.sportsman_1, self.sportsman_3)
        # Старт, и в словарь "all_result" записываем результат функции как (место:имя)
        all_results = self.compete.start()
        # имя последнего спортсмена
        self.last_runner = all_results[max(all_results.keys())].name
        self.assertTrue(self.last_runner == 'Ник')  # вызываем юнит-метод, сравниваем (True)
        TournamentTest.all_results[1] = all_results  # записываем словарь с ключом 1

    def test_second_race(self):

        # создаем объект класса Соревнование
        self.compete = run_tur.Tournament(90, self.sportsman_2, self.sportsman_3)
        # Старт, и в словарь "all_result" записываем результат функции как (место:имя)
        all_results = self.compete.start()
        # имя последнего спортсмена
        self.last_runner = all_results[max(all_results.keys())].name
        self.assertTrue(self.last_runner == 'Ник')  # вызываем юнит-метод, сравниваем (True)
        TournamentTest.all_results[2] = all_results  # записываем словарь с ключом 2

    def test_third_race(self):

        # создаем объект класса Соревнование
        self.compete = run_tur.Tournament(90, self.sportsman_1, self.sportsman_2, self.sportsman_3)
        # Старт, и в словарь "all_result" записываем результат функции как (место:имя)
        all_results = self.compete.start()
        # имя последнего спортсмена
        self.last_runner = all_results[max(all_results.keys())].name
        self.assertTrue(self.last_runner == 'Ник')  # вызываем юнит-метод, сравниваем (True)
        TournamentTest.all_results[3] = all_results  # записываем словарь с ключом 3

if __name__ == '__main__':
    unittest.main()
