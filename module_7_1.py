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
        file = open(self.__file_name, 'r')
        self.all_products = file.read()
        file.close()
        return self.all_products

    def add(self, *products):       # Добавляет в файл __file_name каждый продукт из products,
                                    # если его ещё нет в файле (по названию)
        self.products = products

        for name_products in self.products:
            if self.get_products().find(f'{name_products.name}') == -1:
                __file_name = open(self.__file_name, 'a')
                __file_name.write(f'{name_products}\n')
                __file_name.close()
            else:
                pprint (f'Продукт {name_products} уже есть в магазине')

#__________________________________________
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
# pprint()

print(s1.get_products())
