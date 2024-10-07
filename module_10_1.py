from time import sleep
from datetime import datetime
from threading import Thread

# time_start = datetime.now()

def write_words(word_count, file_name):  # количество записываемых слов, и куда будут записываться слова.

    text = 'Волшебство'
    index = 0
    while index < word_count:
        with open(file_name, 'a', encoding='utf-8') as file:  # открытие файла 'a', append в файл
            file.write(rf'{text} №{index + 1} \n'.format(f=index))     # запись в файл
            sleep(0.1)              # Задержка на 0.1 секунды
            index += 1
    print(f"Завершилась запись в файл {file_name}.")

time_start_1 = datetime.now()   # время начала первой части
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_1 = datetime.now()     # время конца первой части
time_result_1 = time_end_1 - time_start_1
print(time_result_1)

time_start_2 = datetime.now()   # время начала второй части
thr_first = Thread(target= write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_2 = datetime.now()     # время конца второй части
time_result_2 = time_end_2 - time_start_2
print(time_result_2)