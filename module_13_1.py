import logging
import time
import asyncio

'''Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
Напишите асинхронную функцию start_strongman(name, power), где name - имя силача,
power - его подъёмная мощность. Реализуйте следующую логику в функции:

1.	В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
2.	После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно
     пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
3.	В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
'''
logging.basicConfig(
    filename='strongman_tests.log', level=logging.INFO, filemode='a', encoding='UTF-8')
logging.debug('tests_12_4')
logging.info('Finished')

start = time.time()                      # Старт соревнований
cargo_form_ball = {'1':25, '2': 30, '3': 35, '4': 40, '5': 45}

async def start_strongman(name, power):     # имя и подъёмная мощность силача
    start = time.time()                      # Старт участника "name"
    cargo_form = cargo_form_ball.items()    # подготовка словаря
    print(f'Силач {name} начал соревнования.')  #
    for key, ball in cargo_form:  #
        print(f'Силач {name} поднял шар № {key}')  #
        time_cargo = ball / power             # Вычисление времени задержки
        await asyncio.sleep(time_cargo)  #
    print(f'Силач {name} выполнил программу за {time.time() - start:.4f} сек.')
    print(f'Силач {name} закончил соревнования.')

'''Также напишите асинхронную функцию start_tournament, в которой 
создаются 3 задачи для функций start_strongman. Имена(name) и силу(power) 
для вызовов функции start_strongman можете выбрать самостоятельно.
После поставьте каждую задачу в ожидание (await).
Запустите асинхронную функцию start_tournament методом run.
'''
async def start_tournament():

    print(f'Старт участника')
    strongman = {'Антон': 60, 'Гоша': 55, 'Егор': 50}   # имя и подъёмная мощность силача
    play = strongman.items()  # подготовка словаря
    the_lot = [start_strongman(k, v) for k, v in play] # цикл с запуском функции "start_strongman"
    await asyncio.gather(*the_lot)  # функция, которая позволяет запускать несколько корутин
    # или ожидаемых объектов параллельно и получать результаты после их завершения

asyncio.run(start_tournament())           # Запуск программы
finish = time.time()                      # Финиш соревнований
print(f'Wasted my time = {round((finish - start))} seconds')