from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup  # Состояние
# from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # всплывающая клавиатура внизу
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # клавиатура

from crud_functions import *
import asyncio
import logging


api = "8141485832:AAF6UoDN1lQ9PcBsyHh1z3AqgY0P-yMcQLs"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

'''Инициализация инлайн клавиатуры каталога'''
ccal_ikb= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas'),
    InlineKeyboardButton(text='Вернутся', callback_data='back')]
    ]
)         # инициализация инлайн клавиатуры
'''Инициализация инлайн клавиатуры продукции'''
catalog_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product 1', callback_data='product_buying'),
    InlineKeyboardButton(text='Product 2', callback_data='product_buying'),
    InlineKeyboardButton(text='Product 3', callback_data='product_buying'),
    InlineKeyboardButton(text='Product 4', callback_data='product_buying')],
    [InlineKeyboardButton(text='Вернутся', callback_data='back')]
    ]
)

'''добовляем кнопки в клавиатуру + размер кнопок'''
user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Норма ккал'),
         KeyboardButton(text='Купить'),
         KeyboardButton(text='Информация')]
    ], resize_keyboard= True
)

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пользователи', callback_data='product_buying')],
    [],
    [


    ]
])

class UserState(StatesGroup):
    age = State()               # Возраст
    growth = State()            # Рост
    weight = State()            # Вес

@dp.message_handler(commands=['start'])
async def start(message):
    print('Я бот помогающий твоему здоровью.')
    await message.answer(f'Добро пожаловать:\n'     
                         f'Ваш выбор"', reply_markup=user_menu)  # вывод кнопок kb

@dp.message_handler(text= 'Норма ккал')
async def main_menu(message):        #
    '''выводим пользователю сообщение и клавиатуру'''
    await message.answer(f'Выберите опцию:', reply_markup= ccal_ikb)

@dp.message_handler(text= 'Купить')
async def get_buying_list(message):  # вызов функции get_all_products()
    get_all_products()
    total_base = get_all_products()
    # print(total_base)
    def info_list():
        info_product = []
        for i in total_base:
            product_info = [
                f'Название: {i[1]} |'
                f' Описание: {i[2]} |'
                f' Цена: {i[3]}']
            info_product.append(product_info)
        # print(info_product)
        return info_product
    info_list()
    '''Открываем файл и читаем фото, название картинки 'img', чтение 'rb'.и выводим пользователю сообщение '''

    for i in range(4):
        with open(f"files/v_{i + 1}.png", "rb") as img:
            '''отправить изображение + описание пользователю'''
            await message.answer_photo(img, info_list()[i])
    await message.answer(f'Выберите продукт для покупки:', reply_markup=catalog_ikb)  #


@dp.message_handler(text= 'Информация')
async def get_formulas(message):
    '''выводим пользователю сообщение'''
    await message.answer('1. Расчёт ккал по формуле Миффлина-Сан Жеора.\n'
                         '2. У нас есть витамины для вас!')

@dp.callback_query_handler(text= 'back')
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=user_menu)
    await call.answer()

@dp.callback_query_handler(text= 'product_buying')
async def send_confirm_message(call):
    '''выводим пользователю сообщение'''
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
    print('Вы успешно приобрели продукт!')

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
    await call.message.answer(f'Выберите опцию:', reply_markup=ccal_ikb)
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

# '''Загрузка фото'''
# from aiogram import Bot, Dispatcher, executor, types
#
# API_TOKEN = 'BOT_TOKEN_HERE'
#
# # Configure logging
# import logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(API_TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler(content_types=['photo'])
# async def process_photos(message: Message):
#     for i, photo in enumerate(message.photo):
#         async with bot.download_file(photo.file_id) as file:
#             with open(f"photo_{i}.jpg", "wb") as f:
#                 f.write(file)
#     await bot.send_message(
#         chat_id=message.chat.id, text="Фото получены"
#     )
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)