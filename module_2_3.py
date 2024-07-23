
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # Нужно выписывать из этого списка только положительные числа до
    # тех пор, пока не встретите отрицательное или не закончится список
index = 0           # переменная

while index < len(my_list):
    if my_list[index] % 2 == 0 and my_list[index] != 0:
        print(my_list[index])
        index += 1
    else: index += 1