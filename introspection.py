import inspect
from pprint import pprint

# Испытательный код
some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)

some_object = SomeClass

# some_class_method(value=some_string)
# check_param(value=some_list)
#---------------------------------------------------------

# "ИНТРОСПЕКЦИЯ"
#
(f'ВВЕДИТЕ ОБЪЕКТ в "may_object"!')

may_object = some_function

print(f'Объект вызывается: {callable(may_object)}')  # можно ли вызвать объект
try:
    print(f'Имя объекта: {may_object.__name__}')
except:
    pass
try:
    print(f'Значение объекта: {inspect.signature(may_object)}') # подпись вызываемого объекта
except:
    pass
print(f'объект является модулем: {inspect.ismodule(may_object)}') # Возвращает True, если объект является модулем
print(f'объект является классом: {inspect.isclass(may_object)}') # Возвращает True, если объект является классом.
print(f'объект является функцией: {inspect.isfunction(may_object)}') # Возвращает True, если объект является
                                            # функцией включая функции, созданные с помощью лямбда-выражений....
print(f'объект является встроенной функцией '
      f'или связанным встроенным методом: {inspect.isbuiltin(may_object)}') # Возвращает True, если объект
                                    #  является встроенной функцией или связанным встроенным методом.
print(f'объект является кодом: {inspect.isbuiltin(may_object)}') # Возвращает True, если объект является кодом

print(f'Тип объекта: {type(may_object)}')

def introspection_info(obj):
    inf = dir(obj)
    return inf

number_info = introspection_info(may_object)
print(number_info)      # Лист
# pprint(number_info)   # Строка

# print(f'Aтрибут {name}: {getattr(may_object, name[, default])}')  #
                  # name : str - Имя атрибута, значение которого требуется получить

# Является ли объект экземпляром определенного типа или определенного пользователем класса
# print(isinstance(may_object, int))