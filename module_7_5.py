import os, pathlib, time
from pprint import pprint

directory = '.'
file = []
for root, dirs, files in os.walk(directory):   # все файлы директории
    for this_entry in files:
        file.append(this_entry)

filename = file[0]                     # имя файла

pathfile = os.getcwd()                          # возвращает текущий рабочий каталог
filepath = os.path.join(pathfile, filename)       # полный путь к файлу
filetime = os.path.getmtime(str(filepath))               # время действия файла
formatted_time = {time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))}
#                                                    # формат и отформатированние времени
filesize = {os.path.getsize(filepath)}         # {os.path.getsize}    # размер файла
parent_dir = os.path.dirname(filepath)         # родительский каталог

# pprint(filepath)
pprint(f'Обнаружен файл: {filename}, Путь: {pathfile},'
          f' Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')
