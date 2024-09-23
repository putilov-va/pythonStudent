from pprint import pprint

class Product:      # Продукты '<название>, <вес>, <категория>'
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

     def get_products(self):
        file = open(self.__file_name, 'r')  # чтение файла
        all_products = file.read()
        file.close()
        return all_products

    def add(self, *products):       # Добавляет в файл __file_name каждый продукт из products,
                                    # если его ещё нет в файле (по названию)
        all_products = self.get_products()
        file = open(self.__file_name, 'a') # открываем "добавить"

        for product in products:
            if str(product) not  in all_products:
                file.write(str(product) + '\n') # добовляем продукт
                all_products += str(product) + '\n'
            else:
                pprint (f'Продукт {product} уже есть в магазине')
        file.close()
#__________________________________________
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
