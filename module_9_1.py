def apply_all_func(int_list, *functions):         # Список из чисел (int, float), и функции
    results = {}                                  # Создаём словарь
    for func_tion in functions:                   # Перебор функций в списке функций
        results[func_tion.__name__] = str(func_tion(int_list))  # Исползуя метод __name__ добавляем в список словари,
                                                                # где ключ - имя функции, значение - результат работы
                                                                #  функции: func_tion(int_list)
    return results                                # Возвращаем словарь


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
