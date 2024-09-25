import os, pathlib, time
from pprint import pprint

files = os.listdir()
file = {this_entry for this_entry in files if not os.path.isdir(this_entry)}   # имя файла

pathfile = os.getcwd()                                  # путь к файлу
filepath = os.path.join(pathfile, *file)       # полный путь к файлу
filetime = os.path.getmtime(str(filepath))               # время действия файла
formatted_time = {time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))}
#                                                    # отформатированное время
filesize = {os.path.getsize(filepath)}         # {os.path.getsize}    # размер файла
parent_dir = os.path.dirname(filepath)         # родительский каталог

# print(file)
# pprint(pathfile)
# # pprint(formatted_time)
# pprint(filepath)
pprint(f'Обнаружен файл: {file}, Путь: {pathfile},'
          f' Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')

#
# all_entries = os.listdir()
#
# files = {entry for entry in all_entries if not os.path.isdir(entry)}   # имя файла
# directories = [entry for entry in all_entries if os.path.isdir(entry)]
#
# print('Files:', files)
# print('Directories:', directories)
