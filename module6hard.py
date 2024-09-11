import math
class Figure:
    '''Геометрические фигуры'''
    sides_count = 0                  # количество сторон, рёбер


    def __init__(self, color, *sides):
        self.__color = list(color)    # цвет стороны RGB
        self.filled = False           # закрашенный
        self.__sides = sides
        if len(self.__sides) == self.sides_count:
            self.__sides = self.__sides * self.sides_count
        else:
            self.__sides = [1] * self.sides_count  # список рёбер
        # self.__sides = sides if len(sides) == self.sides_count else [1] * self.sides_count  # список рёбер

    def get_color(self):            # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверка корректности
        Figure.set_color(r, g, b)
        if r % 1 == 0 or g % 1 == 0 or b % 1 == 0:
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.__is_valid_color == True:
            self.__color = [r, g, b]

    def get_color(self):    # возвращает список RGB цветов
        return self.__color

    def get_sides(self):
        return self.__sides

# print(cube1.get_sides())
    def __len__(self):              # периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            pass

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        # super().__init__(color, sides)
        self.__sides = sides            # сторона у круга всего 1
        self.__radius = self.__sides / (2 * math.pi)
        super().__init__(color, sides)

    def radius(self):
        return self.__sides / (2 * math.pi)

    def get_square(self):               # площадь круга
        square = (self.__sides ** 2) / (4 * math.pi)
        return square

class Triangle(Figure):
    sides_count = 3

    def get_square(self, a, b, c):               # площадь треугольника
        self.a_ = a
        self.b_ = b
        self.c_ = c
        p = (self.a_ + self.b_ + self.c_) / 2
        square = math.sqrt(p * (p - self.a_) * (p - self.b_) * (p - self.c_))
        return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        self.__sides = sides
        super().__init__(color, sides)

    def get_sides(self):
        return self.__sides

    def get_volume(self):               # площадь куба
        volume = self.__sides ** 3
        return volume


# issubclass(Cube, Figure)
# print(Cube.mro)
#_______________________________________________________
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# triangle1 = Triangle((44, 120, 245), 3)

    # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# triangle1.get_square(4, 5, 6)
# print(triangle1.get_square)

   # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides (15)  # Изменится
print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
print(len(circle1))

    # Проверка объёма (куба):
print(cube1.get_volume())

# #_______________________________________
# #___________________________________
# #___________________________________
#___________________________________________

# class Figure:
#     '''Геометрические фигуры'''
#     sides_count = 0             # количество сторон рёбер
#     filled = False              # закрашенный
#
#     def __init__(self, color, sides):
#         self.__sides = sides    # длинна рёбер
#         self.__color = color    # цвет стороны RGB
#         # self.filled = filled    # закрашенный
#
#     def get_color(self):    # возвращает список RGB цветов
#         return self.__color
#
#     def __is_valid_color(self, r, g, b):  # проверка корректности
#         # self.set_color(self, r, g, b)
#         if r % 1 == 0 or g % 1 == 0 or b % 1 == 0:
#         # if (r, g, b) in self.set_color(r, g, b):
#             if int(r) >= 0 or int(r) < 255:
#                 if int(g) >= 0 or int(g) < 255:
#                     if int(b) >= 0 or int(b) < 255:
#                         result = True
#                     else:
#                         result = False
#                     return result
#
#     def set_color(self, r, g, b):
#         # self.__is_valid_color()
#         # self.__color = color
#         self.r = r
#         self.g = g
#         self.b = b
#         if self.__is_valid_color == True:
#             self.__color = self.color
#         else:
#             pass
#
#     def __is_valid_sides(self):
#         if self.sides_count % 1 == 0 and self.sides_count > 0 and self.sides_count == self.sides_count:
#             return True
#         else:
#             return False
#
#     def get_sides(self):
#         if self.__is_valid_sides == True:
            # if len(self.sides_count) == len(self.__sides):
            #     for i in  range(1, self.sides_count + 1):
            #         return [self.__sides]
            # else:
            #     for i in range(1, self.sides_count + 1):
            #  #       return [1]
#             return self.__sides
#
#     def __len__(self):
#         return (self.__sides * self.sides_count)
#
#     def set_sides(self, *new_sides):
#         if new_sides == self.sides_count:
#             self.__sides = new_sides
#         else:
#             pass
#
# class Circle(Figure):
#     sides_count = 1
#     __radius = 0
#
#     def radius(self):
#         self.__sides / (2 * math.pi)
#         return self.__radius
#
#     def get_square(self):               # площадь круга
#         return (self.__sides ** 2) / (4 * math.pi)
#
# class Triangle(Figure):
#     sides_count = 3
#
#     def get_square(self, a, b, c):               # площадь треугольника
#         self.a_ = a
#         self.b_ = b
#         self.c_ = c
#         p = (self.a_ + self.b_ + self.c_) / 2
#         square = math.sqrt(p * (p - self.a_) * (p - self.b_) * (p - self.c_))
#         return square
#
# class Cube(Figure):
#     sides_count = 12
#
#     def __init__(self, color, sides):
#         super().__init__(color, sides)
#
#     def get_sides(self):
#         return self.__sides
#
#     def get_volume(self):               # площадь куба
#         volume = self.__sides ** 3
#         return volume
