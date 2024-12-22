import sqlite3

'''Создаём структуру базы данных (setup) - файл с "именем", и расширением "db" '''
connection = sqlite3.connect('initiate_d_b.db')
initiate = connection.cursor() # взаимодействие с базой данных

'''Для создания таблицы в базе данных используется команда 'CREATE TABLE' ('CREATE' означает 
создание таблицы, а  'IF NOT EXISTS' это проверка, если она не существует, 'Products' имя таблици). 
  Ключевые команды пишутся заглавными буквами, а названия таблиц — с большой буквы. 
Набор полей: 1.	id - целое число, первичный ключ.  2. title(название продукта) - текст (не пустой)
3.	description(описание) - текст.  4.	price(цена) - целое число (не пустой)'''

initiate.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL   
)
''')

product_name = ['"Сила"', '"Век"', '"Тру-ля-ля"', '"Тра-ля-ля"']

price00 = [100, 150, 200, 250]

'''1) созданиe индекса "idx_title" ускоряет поиск данных в базе данных '''
# initiate.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title, description, price)')

'''2) Добавь продукт + проверка на присутствие'''
# def add_product(title, description, price):
#     check_product = initiate.execute('SELECT * FROM Products WHERE id=?', __parameters=title)
#     if check_product.fetchone() is None:
#         initiate.execute(f'''INSERT INTO Users VALUES('{title}', '{description}', 0)
# ''')
#     connection.commit()  # сохраняет все изменения

'''3) запрос, который будет Добавлять данные в таблицу '''
# def initiate_d_b():
#     for i in range(4):
#         initiate.execute(
#             'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#             (f'product_{i + 1}',  f'{product_name[i]}', f'{price00[i]}'))  # добавить 4 строки данных
#     connection.commit()
# initiate_d_b()

'''4) запрос, на Удаление определённых строк из таблицы '''
# for i in range(1, 20, 3):
#     initiate.execute(
#         'DELETE FROM Products WHERE title = ?',
#         (f'title{i}',))  # удалить каждую третью строку


'''10) Чтение данных «*» - всей строки'''
def get_all_products():
    '''Создаём структуру базы данных (setup) - файл с "именем", и расширением "db" '''
    connection = sqlite3.connect('initiate_d_b.db')
    initiate = connection.cursor()  # взаимодействие с базой данных

    initiate.execute('SELECT * FROM Products')  # id=?', (f'2',))
    '''  Применять 'fetchone()' или 'fetchall()' — это ключ к успешной работе
     с базами данных и эффективному управлению полученной информацией'''
    ''' Сколько извлечь - весь столбик запроса'''
    database = initiate.fetchall()
    # return database
    return database

    connection.commit()  # сохраняет все изменения
    connection.close()  # закрыть соединение с базой данных
# get_all_products()

'''  Применять 'fetchone()' или 'fetchall()' — это ключ к успешной работе
        с базами данных и эффективному управлению полученной информацией'''


# get_all_products()

connection.commit() # сохраняет все изменения
connection.close()  # закрыть соединение с базой данных

#     '''  Применять 'fetchone()' или 'fetchall()' — это ключ к успешной работе
#         с базами данных и эффективному управлению полученной информацией'''
#
#     # ''' Баланс всех пользователей по "price"'''
#     initiate.execute('SELECT SUM (price) FROM Products')
#     prices = initiate.fetchone()[0]
#     info_products = []
#     for i in range(database):
#         info_products.append(i + 1)
#
#     print(info_products)  # средний баланс всех пользователей
#     print(prices)
#     print(database)
#
#
# get_all_products()