grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # оценки
print(type(grades), grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students), students)

grades_avar = [sum(grades[0]) / len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[-1])/len(grades[-1])]
print(type(grades_avar), grades_avar)             # список средних значений списка "grades"
students_sort = sorted(students)                  # сортированный список студентов
print(type(students_sort), students_sort)
students_grade = dict(zip(students_sort, grades_avar)) # объеденяем списки в словарь
print(type(students_grade), students_grade)