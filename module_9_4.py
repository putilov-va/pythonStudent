first = 'Мама мыла раму'
second = 'Рамена мало было'

#eguality = lambda x, y: x == y # функция равенства элементов списка
letter_matches = list(map(lambda x, y: x == y, first, second)) # функция применяется одновременно к двум спискам
print(letter_matches)
#_____________________________________________________________
# from pathlib import Path
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as fail_txt:
            for element in data_set:

                fail_txt.write(str(element) + '\n') # текст на запись
    return write_everything

writers = get_advanced_writer('example.txt')
writers('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#________________________________________________
from random import choice
class MysticBall():

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)   # выбор случайных слов
        # for word in choice(self.words): # не доработал
        #     return word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
