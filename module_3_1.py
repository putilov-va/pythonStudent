
calls = 0
def count_calls ():
    global calls
    calls+=1            # Счётчик обращений к "count_calls"
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
   # Возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
def is_contains (string, list_to_search):
    count_calls()
    return string.lower() in [string.lower() for string in list_to_search]
    # Проверка если строка находится в этом списке: то True

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)


