from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup  # Состояние
# from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # всплывающая клавиатура внизу
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # клавиатура
import asyncio

api = "8141485832:AAF6UoDN1lQ9PcBsyHh1z3AqgY0P-yMcQLs"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

ikb = InlineKeyboardMarkup()         # инициализация инлайн клавиатуры
# ikb = InlineKeyboardMarkup()      # инициализация инлайн клавиатуры
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')  # создание кнопки
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')  # создание кнопки
ikb.add(button3)                     # добовляем кнопку в клавиатуру
ikb.add(button4)

# добовляем кнопки в клавиатуру + размер кнопок
user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'),
         KeyboardButton(text='Информация')]
    ], resize_keyboard= True
)

'''Норма калорий для человека'''

class UserState(StatesGroup):
    age = State()               # Возраст
    growth = State()            # Рост
    weight = State()            # Вес

@dp.message_handler(commands=['start'])
async def start(message):
    print('Я бот помогающий твоему здоровью.')
    await message.answer(f'Узнать норму калорий на сутки для мужчин:\n'     
                         f'введите "Рассчитать"', reply_markup=user_menu)  # вывод кнопок kb

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):        #
    '''выводим пользователю сообщение и клавиатуру'''
    await message.answer(f'Выберите опцию:', reply_markup= ikb )  #
    # await UserState.age.set()       # ждём введения

@dp.message_handler(text= 'Информация')
async def get_formulas(message):
    '''выводим пользователю сообщение'''
    await message.answer('Формула Миффлина-Сан Жеора.')

@dp.message_handler()
async def all_messages(message):
    print('Привет!')
    await message.answer(f'Привет! \n'
                         f'Для начала работы введите "/start"')

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    '''выводим пользователю сообщение'''
    await call.message.answer('Формула Миффлина-Сан Жеора.\n '
                              'Формула , разработанная группой американских врачей-диетологов '
                              'под руководством докторов Миффлина и Сан Жеора, существует в двух'
                              ' вариантах – упрощенном и доработанном и выдает необходимое количество'
                              ' килокалорий (ккал) в сутки для каждого конкретного человека.\n'
                              'Упрощенный вариант формулы Миффлина-Сан Жеора:\n '
                              'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n '
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()

@dp.callback_query_handler(text= 'calories')
async def set_age(call: types.CallbackQuery):        # Возраст
    '''выводим сообщение пользователю'''
    await call.message.answer(f'Введите свой возраст:')
    await UserState.age.set()       # ждём введения возраста (age) методом (set)
    await call.answer()

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
    print(calories)

    await message.answer(
        f'Для оптимального похудения или сохранения нормального веса вам '
        f'требуется {calories} ккал.'
            )
    await state.finish()

@dp.message_handler()
async def all_messages(message):
    print('Привет!')
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.\n'
                         f'Для начала работы введите "/start"')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
