first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# высчитывает разницу длин строк из списков
first_result = (len(x)-len(y) for (x, y) in zip(first, second) if len(x) != len(y))

# результаты сравнения длин строк в одинаковых позициях из списков
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))

print(list(first_result))
print(list(second_result))

