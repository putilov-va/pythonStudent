first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
# длина строк не менее 5 символов

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
# список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины.
# Каждое слово из списка first_strings должно сравниваться с каждым из second_strings.

third_result = {y: len(y) for list_ in (first_strings, second_strings) for y in list_ if len(y) // 2}
# Условие записи пары в словарь - чётная длина строки

print(first_result)
print(second_result)
print(third_result)