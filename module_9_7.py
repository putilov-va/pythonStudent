def is_prime(*func):        # Функция декоратор
    def wrapper(*args):     # функция определения чисел простых и состаных
        result = sum(args)   # сумма поступивших чисел
        from math import sqrt

        check = True                # проверка
        divider = 2                  # делитель
        while divider <= sqrt(result):   # sqrt - возвращает квадратный корень числа
            if result % divider == 0:    # остаток отделения
                check = False
                break
            divider += 1

        if check:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    summa = sum(args)   # сумма поступивших чисел
    return summa

result = sum_three(2, 3, 6)
print(result)
