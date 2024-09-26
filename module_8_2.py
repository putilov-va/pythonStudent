
def personal_sum(*numbers):         # функция возвращает кортеж из двух значений
    incorrect_data = 0
    result = 0


    for number_in in numbers:
        for number in number_in:
            try:
                result += number

            except TypeError as exc:
                incorrect_data += 1
                print(f'некорректный тип данных для подсчета суммы - {number}')


    return result, incorrect_data

def calculate_average(*numbers):        # Среднее арифметическое значение

    if isinstance(*numbers, float) or isinstance(*numbers, int):
        print (f'В numbers записан некорректный тип данных')
        return None

    try:
        sum_result = personal_sum(*numbers)
        return sum_result[0] / (len(*numbers) - sum_result[1])

    except ZeroDivisionError:  # при делении на 0
        return 0



# # ## Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

# print(incorrect_data)

###_____________________________________________________
#
# def personal_sum(*numbers):
#     result = 0
#     incorrect_data = 0
#     for i in numbers:
#         # print(i)
#         for j in i:
#             # print(j)
#             try:
#                 result += j
#             except TypeError:
#                 incorrect_data += 1
#                 print(f'некорректный тип данных для подсчета суммы - {j}')
#     return result, incorrect_data
#
# def calculate_average(*numbers):
#     if isinstance(*numbers, int):
#         return None
#     try:
#         tuple_pers_sum = personal_sum(*numbers)
#         # print(tuple_pers_sum[0])
#         # print(len(*numbers))
#         # print(tuple_pers_sum[1])
#         #return sum(numbers) / len(numbers)
#         return tuple_pers_sum[0] / (len(*numbers) - tuple_pers_sum[1])
#     except ZeroDivisionError:
#         return 0
#     except TypeError:
#         return f'В numbers записан некорректный тип данных'
#
# print(f'Результат 1: {calculate_average("1, 2, 3")}')
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
# print(f'Результат 3: {calculate_average(567)}')
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
# #______________________________
