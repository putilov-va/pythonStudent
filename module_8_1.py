# add_everything_up(a, b) принимает a и b, которые могут быть
# как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в
# том же порядке). Во всех остальных случаях выполнять стандартные действия.
def add_everything_up(a, b):    # складывать числа(int, float) и строки(str)
    try:

        result = a + b
        return round(result, 3)   # округление числа до третьего знака

    except TypeError:
        return f'{a}{b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


#________________________________________________
# import os, pathlib, time
# from pprint import pprint
#
# # def notes_counter():
# # os.mkdir('dir_module_7')
# # files = os.walk('.')
# for root, dirs, files in os.walk('.'):   # где ('.') -текущая директория
#     for file in files:
#
#         file = {d for d in os.listdir() if os.path.isfile(d)}
#
#         filepath = os.getcwd()    # путь к файлу
#
#     # for dir in  dirs:
#     #     parent_dir = {os.path.dirname}  # pathlib.Path.parent
#     # for root in os.walk('.'):  # ('.') -текущая директория
#
#     # for r in root:
#
#         filetime = os.path.getmtime   # время действия файла
#
#         # filetime = {filetime.decode()}
#         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#             #             # отформатированное время
#         filesize = {os.path.getsize}         # {os.path.getsize}    # размер файла
#         parent_dir = {os.path.dirname}    # pathlib.Path.parent #(r'D:\2Рабочая\ACER D\module_7_4\module_7_4.py')      # родительский каталог
#         # break
#
#
# pprint(filetime)
# pprint(f'Обнаружен файл: {file}, Путь: {filepath},'
#           f' Размер: {filesize} байт, Время изменения: {formatted_time},'
#           f' Родительская директория: {parent_dir}')
# print(type(filesize))
# print(type(formatted_time))
# print(type(parent_dir))
# print(type(filetime))
