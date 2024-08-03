
def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25),
print_params(c = [1,2,3])

values_list = ['line', 19, (1, 2, 3)]
print_params(*values_list)

values_dict = {'a' : 4, 'b' : "line", 'c' : False}
print_params(**values_dict)

values_list_2 = ['Строка', 25.52 ]
print_params(*values_list_2, 42)