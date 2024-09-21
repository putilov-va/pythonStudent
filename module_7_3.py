# from pathlib import Path
import string
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names    # чтение файла в файл
        # self.path = Path(file_names)    # чтение имени файла

    def get_all_words(self):
        self.all_words = {}

        for file_new in self.file_names:
            with open(file_new, 'r', encoding='utf-8') as file:
                text_low = file.read()
                text_punct = list(string.punctuation)
                for punct in text_punct:    # удоляем [',', '.', '=', '!', '?', ';', ':', ' - ']
                    if punct in text_low:
                        text_now = text_low.replace(punct, '')
                        text_now = text_now.split()      # разделение строки по пробелу
                self.all_words[file_new.lower()] = text_now
                return self.all_words

    def find(self, word):  # ключ - название файла
                            # значение - позиция первого такого слова в списке слов этого файла
        self.word = word
        results = {}
        for name, words in self.get_all_words().items(): # возвращает список с парами всех ключей и значений словаря
            if word.lower() in words:
                results[name] = words.index(word.lower()) + 1  # позиция первого (такого) слова
        return results

    def count(self, word):  # ключ - название файла,
                            # значение - количество слова word в списке слов этого файла
        self.word = word
        results = {}
        for name, words in self.get_all_words().items(): # возвращает список с парами всех ключей и значений словаря
            if word.lower() in words:   # количество (данного) слова в списке слов этого файла
                quantity = words.count(word.lower())
                if quantity > 0:
                    results[name] = quantity
        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
