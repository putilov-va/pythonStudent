

nums = int(input('Введите одно число от 3 до 20: '))
def gen_cod():
    coder = ""

    for i in range(1, nums):           # перебор чисел до i
        for j in range(i + 1, nums):   # перебор чисел до j, и уникальность
            if nums % (i + j) == 0:    # проверяем кратность числа nums
                coder += f'{i}{j} '    # вывод пары чисел каждого перебора

    print(nums, '-', coder)
gen_cod()

