from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup  # Состояние
# from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # всплывающая клавиатура внизу
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # клавиатура
import asyncio
import logging

api = ""
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

catalog_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Product 1', callback_data='product_buying'),
    InlineKeyboardButton(text='Product 2', callback_data='product_buying'),
    InlineKeyboardButton(text='Product 3', callback_data='product_buying'),
    InlineKeyboardButton(text='Product 4', callback_data='product_buying')],
    [InlineKeyboardButton(text='Вернутся', callback_data='back')]
    ]
)         # инициализация инлайн клавиатуры

# добовляем кнопки в клавиатуру + размер кнопок
user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Норма ккал'),
         KeyboardButton(text='Купить'),
         KeyboardButton(text='Информация')]
    ], resize_keyboard= True
)

'''"Витамины для всех!"'''

class UserState(StatesGroup):
    age = State()               # Возраст
    growth = State()            # Рост
    weight = State()            # Вес

product_name1 = '"Сила"'
product_name2 = '"Век"'
product_name3 = '"Тру-ля-ля"'
product_name4 = '"Тра-ля-ля"'

price1 = 100
price2 = 150
price3 = 200
price4 = 250

products = [
    f'Название: product_1 | Описание: {product_name1} | Цена: {price1}',
    f'Название: product_2 | Описание: {product_name2} | Цена: {price2}',
    f'Название: product_3 | Описание: {product_name3} | Цена: {price3}',
    f'Название: product_4 | Описание: {product_name4} | Цена: {price4}'
]

@dp.message_handler(commands=['start'])
async def start(message):
    print('Я бот помогающий твоему здоровью.')
    await message.answer(f'Добро пожаловать:\n'     
                         f'Ваш выбор"', reply_markup=user_menu)  # вывод кнопок kb

@dp.message_handler(text= 'Норма ккал')
async def main_menu(message):        #
    '''выводим пользователю сообщение и клавиатуру'''
    await message.answer(f'Выберите опцию:', reply_markup= ccal_ikb)  #
    # await UserState.age.set()       # ждём введения

@dp.message_handler(text= 'Купить')
async def get_buying_list1(message):        #
    '''Открываем файл и читаем фото, название картинки 'img', чтение 'rb'.и выводим пользователю сообщение '''
    # with open('files/v_1.png', 'rb') as img:  # название картинки 'img', чтение 'rb'.и выводим пользователю сообщение
    #     '''отправить загруженное изображение пользователю'''
    #     await message.answer_photo(img, product_1)

    for i in range(4):
        with open(f"files/v_{i + 1}.png", "rb") as img:
            '''отправить загруженное изображение с описанием пользователю'''
            await message.answer_photo(img, products[i])
    await message.answer(f'Выберите продукт для покупки:', reply_markup=catalog_ikb)  #


@dp.message_handler(text= 'Информация')
async def get_formulas(message):
    '''выводим пользователю сообщение'''
    await message.answer('Расчёт ккал по формуле Миффлина-Сан Жеора.\n'
                         'У нас есть витамины для вас!')

@dp.message_handler()
async def all_messages(message):
    print('Привет!')
    await message.answer(f'Привет! \n'
                         f'Для начала работы введите "/start"')

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

