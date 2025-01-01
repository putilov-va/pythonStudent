import sqlite3


product_name = ['"Сила"', '"Век"', '"Тру-ля-ля"', '"Тра-ля-ля"']

price00 = [100, 150, 200, 250]


def initiate_db():
    '''Создаём структуру базы данных (setup) - файл с "именем", и расширением "db" '''
    connection = sqlite3.connect('initiate_db.db')
    initiate = connection.cursor()  # взаимодействие с базой данных

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

    initiate.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL   
    )
    ''')

    '''1) созданиe индекса "idx_title" ускоряет поиск данных в базе данных '''
    initiate.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

    connection.commit()  # сохраняет все изменения
    connection.close()  # закрыть соединение с базой данных


'''2) Добавь в Products + проверка на присутствие'''
def add_product(title, description, price):
    connection = sqlite3.connect('initiate_db.db')
    initiate = connection.cursor()  # взаимодействие с базой данных

    check_user = initiate.execute('SELECT * FROM Products WHERE id=?', __parameters=title)
    if check_user.fetchone() is None:
        initiate.execute(f'''INSERT INTO Users VALUES('{title}', '{description}', 0)
''')
    connection.commit()  # сохраняет все изменения
    connection.close()  # закрыть соединение с базой данных

'''Внесение в базу данных Users'''
def add_user(username, email, age, balance):
    connection = sqlite3.connect('initiate_db.db')
    initiate = connection.cursor()  # взаимодействие с базой данных

    # check_username = initiate.execute('SELECT * FROM Users WHERE id=?', __parameters=username)
    check_username = initiate.execute('SELECT username FROM Users WHERE username=?',
                                      (username,)).fetchall()
    if not check_username:
        initiate.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                 (f'{username}', f'{email}', f'{age}', f'{balance}')
        )

    connection.commit()  # сохраняет все изменения
    connection.close()  # закрыть соединение с базой данных


'''Проверка на присутствие'''
def is_included(username):
    # print(username)
    connection = sqlite3.connect('initiate_db.db')
    cursor = connection.cursor()  # взаимодействие с базой данных
    check_user = cursor.execute('SELECT username FROM Users WHERE username=?', (username,)).fetchall()

    connection.commit()  # сохраняет все изменения
    connection.close()  # закрыть соединение с базой данных

    if not check_user:
        flag = True
    else:
        flag = False
    return flag


'''3) запрос, который будет Добавлять данные в таблицу Products'''
# def initiate_db():
#     for i in range(4):
#         initiate.execute(
#             'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#             (f'product_{i + 1}',  f'{product_name[i]}', f'{price00[i]}'))  # добавить 4 строки данных
#     connection.commit()
# initiate_db()

'''4) запрос, на Удаление определённых строк из таблицы '''
# for i in range(1, 20, 3):
#     initiate.execute(
#         'DELETE FROM Products WHERE title = ?',
#         (f'title{i}',))  # удалить каждую третью строку


# def add_user(username, age, balance):
#     ''' запрос, который будет Добавлять данные в таблицу '''
#     connection = sqlite3.connect('initiate_db.db')
#     initiate = connection.cursor()  # взаимодействие с базой данных
#
#     for i in range(4):
#         initiate.execute(
#             'INSERT INTO Users (username, age, balance) VALUES (?, ?, ?)',
#             (f'product_{i + 1}',  f'{product_name[i]}', f'{price00[i]}'))  # добавить 4 строки данных
#     connection.commit()
#     initiate_db()
#
#
#
#
#     def initiate_db():
#
#         for i in range(4):
#             initiate.execute(
#                 'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#                 (f'product_{i + 1}',  f'{product_name[i]}', f'{price00[i]}'))  # добавить 4 строки данных
#         connection.commit()
#     initiate_db()

'''10) Чтение данных «*» - всеx строк'''
def get_all_products():
    '''Создаём структуру базы данных (setup) - файл с "именем", и расширением "db" '''
    connection = sqlite3.connect('initiate_db.db')
    initiate = connection.cursor()  # взаимодействие с базой данных

    initiate.execute('SELECT * FROM Products')  # id=?', (f'2',))

    ''' Сколько извлечь - весь столбик запроса'''
    '''  Применять 'fetchone()' - (одно) или 'fetchall()' - (много) — это ключ к успешной работе
            с базами данных и эффективному управлению полученной информацией'''
    database = initiate.fetchall()
    return database

    connection.commit()  # сохраняет все изменения
    connection.close()  # закрыть соединение с базой данных


# class Buyer:  # Покупатель
#
#     def __init__(self, username, age, balance):
#         self.username = username
#         self.age = age
#         self.balance = balance
#
#     def initiate_db(self):
#         '''Создаём структуру базы данных (setup) - файл с "именем", и расширением "db" '''
#         connection = sqlite3.connect('initiate_db.db')
#         initiate = connection.cursor()  # взаимодействие с базой данных
#
#         initiate.execute('''
#         CREATE TABLE IF NOT EXISTS Users(
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         balance INTEGER NOT NULL
#         )
#         ''')
#
#     initiate.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')






'''  Применять 'fetchone()' - (одно) или 'fetchall()' - (много) — это ключ к успешной работе
        с базами данных и эффективному управлению полученной информацией'''

# connection.commit()  # сохраняет все изменения
# connection.close()  # закрыть соединение с базой данных

