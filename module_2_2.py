first = input("Введите число ")
second = input("Введите число ")
third = input("Введите число ")

if first == second and third == second:
    print('Совпало', 3, 'числа')
elif first == second or third == second or first == third:
    print('Совпало', 2, 'числа')
else:
    print('Числа не совпали')