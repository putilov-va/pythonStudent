from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from  aiogram.dispatcher.filters.state import State, StatesGroup # Состояние
from  aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# @dp.message_handler(commands=['start'])
# async def start(message):
#     print('Привет! Я бот помогающий твоему здоровью.')
#     await message.answer(f'Привет! Я бот помогающий твоему здоровью.\n'
#                          f'Узнать норму калорий на сутки: '
#                          f'введите "Calories"')
#
# @dp.message_handler()
# async def all_messages(message):
#     print('Введите команду /start, чтобы начать общение.')
#     await message.answer('Введите команду /start, чтобы начать общение.')


'''Норма калорий для человека'''

class UserState(StatesGroup):   # Состояние
    age = State()               # Возраст
    growth = State()            # Рост
    weight = State()            # Вес

@dp.message_handler(text= 'Calories')
async def set_age(message):        # Возраст
    '''выводим сообщение пользователю'''
    await message.answer('Введите свой возраст:')
    await UserState.age.set()       # ждём введения возраста (age) методом (set)

@dp.message_handler()
async def all_messages(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.\n'
                         f'Узнать норму калорий на сутки для мужчин: '
                         f'введите "Calories"')

@dp.message_handler(state=UserState.age) #
async def set_growth(message, state):        # Рост
    '''сораняем введенное значение (age). методом (update_data).
    метод позволяет обновить данные на введённые'''
    await state.update_data(age=message.text)
    '''выводим сообщение пользователю'''
    await message.answer('Введите свой рост:')
    await UserState.growth.set()  # ждём введения роста (growth) методом (set)

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):        # Вес
    '''сораняем введенное значение (growth) методом update_data.
    метод позволяет обновить данные на введённые'''
    await state.update_data(growth=message.text)
    '''выводим сообщение пользователю'''
    await message.answer('Введите свой вес:')
    await UserState.weight.set()  # ждём введения роста (growth) методом (set)

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):        #
    '''сораняем введенное значение (weight) методом update_data.
        метод позволяет обновить данные на введённые'''
    await state.update_data(weight=message.text)
    '''Сохранить в переменную data все ранее введённые состояния'''
    data = await state.get_data()   # создаётся словарь введённых значений
    '''Формула Миффлина-Сан Жеора для мужчин: 
    calories = 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5'''

    calories = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']))
    # print(calories)

    # @dp.message_handler()
    # async def start(message):
    #     print('Привет! Я бот помогающий твоему здоровью.')
    #     await message.answer(f'Привет! Я бот помогающий твоему здоровью.\n'
    #                          f'Узнать норму калорий на сутки: '
    #                          f'введите "Calories"')

    await message.answer(
        f'Для оптимального похудения или сохранения нормального веса вам '
        f'требуется {calories} килокалорий'
            )
    await state.finish()






# @dp.message_handler(commands=['start'])
# async def start(message):
#     print('Привет! Я бот помогающий твоему здоровью.')
#     await message.answer('Привет! Я бот помогающий твоему здоровью.')
#
# @dp.message_handler()
# async def all_messages(message):
#     print('Введите команду /start, чтобы начать общение.')
#     await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)