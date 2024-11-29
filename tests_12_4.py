import unittest
from runner_and_tournament import  Runner  # Импортируем файл "runner_and_tournament.py"
import logging

logging.basicConfig(
    filename='runner_tests.log', level=logging.INFO, filemode='w', encoding='UTF-8')#,
 # format='%(asctime)s | %(levelnaime)s | %(message)s')

class RunnerTest(unittest.TestCase):

    is_frozen = False
    name_ = 444
    speed_ = -10

    '''Создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого
    объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.'''

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')    # обертка
    def test_walk(self):

        try:
            self.speed_ >=0

            self.sportsman = Runner("Boris", self.speed_)
            for _ in range(10):
                self.sportsman.walk()
            self.assertEqual(self.sportsman.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except BaseException:
            logging.info("Неверная скорость для Runner")

    '''Далее вызовите метод run у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 100.'''

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.name_ == str

            self.sportsman = Runner(self.name_, 9)
            for _ in range(10):
                self.sportsman.run()
            self.assertEqual(self.sportsman.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except BaseException:
            logging.info("Неверный тип данных для объекта Runner")

    '''Далее 10 раз у объектов вызываются методы run и walk соответственно.Т.к. дистанции должны
    быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.'''

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner("Boris")
        runner_2 = Runner("Fedot")
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main(verbosity=2)

#     # '''asctime» — это время обращения, которое позволяет понять,
#     # когда это произошло. «levelname» указывает уровень сообщения:
#     #  «info», «debug», «error», «critical» или «warning».
#     #   А «message» — это то, что мы записываем внутри скобок функций,
#     #    то есть, что именно произошло.'''
#     logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
#                         encoding='UTF-8', format='%(asctime)s || %(levelnaime)s ||'
#                         ' %(message)s', errors=errno.errorcode) #, level=logging.DEBUG)
#     #
#     logging.debug('a')
#     logging.info('b')
#     logging.warning('c')
#     logging.error('d')
#     logging.critical('f')

# # logger = logging.getLogger(__name__)
# def main():
#     logging.basicConfig(filename='runner_tests.log', level=logging.INFO, filemode='a', encoding='UTF-8')
#     # logging.basicConfig(errors=errno.errorcode ,format='%(asctime)s | %(levelnaime)s | %(message)s')
#     # logger.info('Started')
#     # # mylib.do_something()
#     logger.info('Finished')
#
# if __name__ == '__main__':
#     main()
#     logger_.main()