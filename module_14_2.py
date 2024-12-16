import sqlite3

'''Создаём структуру базы данных (setup)'''
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor() # взаимодействие с базой данных

'''Для создания таблицы в базе данных используется команда 'CREATE TABLE' 
('CREATE' означает создание таблицы, а  'IF NOT EXISTS' это проверка, если она не существует). 
Ключевые команды пишутся заглавными буквами, а названия таблиц — с большой буквы. 
Набор полей: 1.	id - целое число, первичный ключ. 2. username - текст (не пустой)
3.	email - текст (не пустой). 4.	age - целое число.
5.	balance - целое число (не пустой)'''

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL   
)
''')

'''1) созданиe индекса "idx_email" ускоряет поиск данных в базе данных '''
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

'''3) запрос, который будет Добавлять данные в таблицу '''
# for i in range(10):
#     cursor.execute(
#         'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#         (f'User{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1) * 10}', '1000'))  # добавить 10 строк данных
'''4) запрос, на Замену в строках "balance" таблицы '''
# for i in range(10):
#     if i % 2 != 0:
#         cursor.execute(
#             f'UPDATE Users SET balance = ? WHERE username = ?',
#             (500, f'User{i}'))  # замена в строках баланса

'''6) запрос, на Удаление определённых строк из таблицы '''
# for i in range(1, 20, 3):
#     cursor.execute(
#         'DELETE FROM Users WHERE username = ?',
#         (f'User{i}',))  # удалить каждую третью строку

'''6.1) запрос, удалить строку в поле "id"'''
# cursor.execute(
#     'DELETE FROM Users WHERE id = ?',
#     (f'6',))  # удалить строку в поле "id" по "№ ?"

'''9) Чтение данных, «*» всех пользователей и Расчёт'''
# cursor.execute('SELECT COUNT (*) FROM Users')
# ''' Сколько клиентов (строк)'''
# total_id = cursor.fetchone()[0]  # извлечь первый элемент результата запроса
# # total2 = cursor.fetchall()     # метод извлекает все строки результата
# #  запроса и позволяет нам работать с ними как с массивом.
# '''  Применять 'fetchone()' или 'fetchall()' — это ключ к успешной работе
#     с базами данных и эффективному управлению полученной информацией'''

'''10) Баланс всех пользователей по "balance"'''
# cursor.execute('SELECT SUM (balance) FROM Users')
# balances = cursor.fetchone()[0]
# print( balances / total_id)  # средний баланс всех пользователей

connection.commit() # сохраняет все изменения
connection.close()  # закрыть соединение с базой данных
