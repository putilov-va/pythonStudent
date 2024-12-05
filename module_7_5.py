import os, time, pathlib

directory = '.'

for root, dirs, files in os.walk(*directory):   # все файлы директории
    for this_entry in files:
        filename = []                            #  - это кортеж имен файлов
        filename.append(this_entry)
        pathfile = os.getcwd()                   # возвращает текущий рабочий каталог
        file_path = os.path.join(pathfile, filename[0])       # полный путь к файлу
        filetime = os.path.getmtime(str(file_path[2]))               # время действия файла
        formatted_time = (time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)))
        #                                               # формат и отформатированние времени
        filesize = (os.path.getsize(file_path[2]))        # {os.path.getsize}    # размер файла
        parent_dir = os.path.dirname(file_path)        # родительский каталог

        print(f'Обнаружен файл: {filename[0]}, Путь: {pathfile},'
                  f' Размер: {filesize} байт, Время изменения: {formatted_time},'
                  f' Родительская директория: {parent_dir}')
