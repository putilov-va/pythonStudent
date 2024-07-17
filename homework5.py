tuple_ = ([1, 2], 3, 4, 'enter')
immutable_var = tuple_
print(immutable_var)
# immutable_var.append('car') # список tuple не изменяемый
tuple_[0][1] = 5
print(immutable_var)
print(type(tuple_))
mutable_list = ['A', 'B', 'C']
mutable_list[2] = 'F'
print(mutable_list)