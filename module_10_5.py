import multiprocessing, time, datetime

file_names = [f'./file {number}.txt' for number in range(1, 5)]  # файлы в текущей дериктории

def read_info(name):

    all_data = []                               # локальный список
    with open(name, encoding='utf-8') as file:  # открытие файла 'r', в файл file
        while True:             # сколько строк неизвестно, запускаем бесконечный итератор
            str_file = file.readline()          # прочитать одну полную строку
            if not str_file:                    # если строки кончились то стоп
                break
            else:
                all_data.append(str_file)        # строки в локальный список

time_start = datetime.datetime.now()  # время начала программы
name = 0
while name < len(file_names):
    read_info(file_names[name])                   # Вызов функции с именем файла
    name += 1
    break
time_end = datetime.datetime.now()    # время конца программы
time_result = time_end - time_start
print(f'{time_result} (линейный)')

if __name__ == '__main__':
    # file_names = [f'./file {number}.txt' for number in range(1, 5)]  # файлы в текущей дериктории
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()    # время начала multiprocessing
        pool.map(read_info, file_names)  # Вызов функции с именем файла
        end = datetime.datetime.now()    # время конца multiprocessing
        print(f'{end - start} (многопроцессный)')


