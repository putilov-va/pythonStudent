
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup  # Состояние
from aiogram.dispatcher import FSMContext
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # всплывающая клавиатура внизу
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # клавиатура

# from  keyboard import *
from crud_functions import *
import asyncio
import logging
import re



logging.basicConfig(level=logging.INFO)
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


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
         KeyboardButton(text='Информация'),
         KeyboardButton(text='Регистрация')]
    ], resize_keyboard= True
)

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пользователи', callback_data='product_buying')],
    [],
    [


    ]
])

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()               # Возраст
    balance = 1000




@dp.message_handler(text='Регистрация')
async def sing_up(message):
    '''выводим пользователю сообщение и клавиатуру'''
    await message.answer(f'Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()  # ждём введения имени, метод (set)


@dp.message_handler(state=RegistrationState.username)  #
async def set_username(message, state):
    in_input = message.text
    '''Проверка вида алфавита'''
    if not re.match(r'^[a-zA-Z]+$', in_input):
        print('Строка должна содержать только латинские буквы и цифры')
        await message.answer(f'Проверьте имя пользователя (только латинский алфавит):\n'
                             f'Ваш выбор', reply_markup=user_menu)  # вывод кнопок kb)
    else:
        print(in_input)

    #     # message.text.encode("iso-8859-1")
        is_username = is_included(message.text)
    #     try:
        if is_username is False:
            await message.answer(f'Пользователь существует, введите другое имя:')
        else:
            '''сохраняем введенное значение (username). методом (update_data).
                                        метод позволяет обновить данные на введённые'''
            await state.update_data(username=message.text)
            '''выводим сообщение пользователю'''
            await message.answer(f'Введите свой email:')
            await RegistrationState.email.set()  # ждём введения email (email), метод (set)
    #
    #     except BaseException as e:
    #         print("Сведения об исключении", e)
    #         await message.answer(f'Проверьте имя пользователя (только латинский алфавит):\n'
    #                              f'Ваш выбор', reply_markup=user_menu)  # вывод кнопок kb)
    #

@dp.message_handler(state=RegistrationState.email)  #
async def set_email(message, state):       # email
    if not ('@' in message.text and message.text.endswith(('.com', '.ru', '.net'))):
        await message.answer(f'Некоректный email. Введите свой email')
    else:
        '''сохраняем введенное значение (age) методом update_data.
            метод позволяет обновить данные на введённые'''
        await state.update_data(email=message.text)
        '''выводим сообщение пользователю'''
        await message.answer('Введите свой возраст:')
        await RegistrationState.age.set()  # ждём введения age (возраст), метод (set)


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):          # Возрастprint(message.text)
    in_input = message.text
    if not re.match(r'^[0-9]+$', in_input):
        await message.answer('Введите свой возраст цифрами:')
        print('Строка должна содержать только цифры')
    else:
        '''сохраняем введенное значение (age) методом update_data.
        метод позволяет обновить данные на введённые'''
        await state.update_data(age=message.text)
        '''Сохранить в переменную data все ранее введённые состояния - создаётся словарь введённых значений'''
        data_user = await state.get_data()
        '''Запись значений в базу'''
        add_user(username=(data_user['username']), email=(data_user['email']),
                 age=(data_user['age']), balance=(str(RegistrationState.balance)))
        '''выводим сообщение пользователю'''
        await message.answer('Поздравляю, вы зарегестрированы.\n Ваш выбор',  reply_markup=user_menu)
        print(f'Регистрация username:', data_user['username'])
        await state.finish()


#----------------------------------------------------------------

class UserState(StatesGroup):
    age = State()               # Возраст
    growth = State()            # Рост
    weight = State()            # Вес

@dp.message_handler(commands=['start'])
async def start(message):
    print('Я бот помогающий твоему здоровью.')
    await message.answer('Добро пожаловать:\n'     
                         'Ваш выбор"', reply_markup=user_menu)  # вывод кнопок kb


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
        return info_product
    info_list()
    '''Открываем файл и читаем фото, название картинки 'img', чтение 'rb'.и выводим пользователю сообщение '''
    # print(info_list())
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
async def set_age(call: types.CallbackQuery):        # calories
    '''выводим сообщение пользователю'''
    await call.message.answer(f'Введите свой возраст:')
    await UserState.age.set()       # ждём введения возраста (age) методом (set)
    await call.answer()

@dp.message_handler(state=UserState.age) #
async def set_growth(message, state):        # Возраст
    '''сораняем введенное значение (age). методом (update_data).
    метод позволяет обновить данные на введённые'''
    await state.update_data(age=message.text)
    '''выводим сообщение пользователю'''
    await message.answer('Введите свой рост:')
    await UserState.growth.set()  # ждём введения роста (growth) методом (set)

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):       # Рост
    '''сораняем введенное значение (growth) методом update_data.
    метод позволяет обновить данные на введённые'''
    await state.update_data(growth=message.text)
    '''выводим сообщение пользователю'''
    await message.answer('Введите свой вес:')
    await UserState.weight.set()  # ждём введения роста (growth) методом (set)

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):         # Вес
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
    # print('Привет!')
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.\n'
                         f'Для начала работы введите "/start"')

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)