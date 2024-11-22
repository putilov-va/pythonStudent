import runner   # Импортируем файл "runner.py"
import unittest

class RunnerTest(unittest.TestCase):
    '''Создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого
    объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.'''

    def test_walk(self):
        sportsman = runner.Runner("Boris")
        for _ in range(10):
            sportsman.walk()
        self.assertEqual(sportsman.distance, 50)

    '''Далее вызовите метод run у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 100.'''

    def test_run(self):
        sportsman = runner.Runner("Fedot")
        for _ in range(10):
            sportsman.run()
        self.assertEqual(sportsman.distance, 100)

    '''Далее 10 раз у объектов вызываются методы run и walk соответственно.Т.к. дистанции должны
    быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.'''

    def test_challenge(self):
        runner_1 = runner.Runner("Boris")
        runner_2 = runner.Runner("Fedot")
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()

# # Код файла "runner.py"
#-------------------------------
# class Runner:
#
#     def __init__(self, name):
#         self.name = name
#         self.distance = 0
#
#     def run(self):
#         self.distance += 10
#
#     def walk(self):
#         self.distance += 5
#
#     def __str__(self):
#         return self.name