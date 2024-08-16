
# def test_function():
#     def inner_function(list_):
#         print(list_)
#
#     # inner_function()
#
#     inner_function("Я в области видимости функции test_function")
#
# test_function()

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
# inner_function()