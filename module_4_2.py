def test_function ():
    def inner_function ():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()
#inner_function() при вызове этой функции, будет выдаваться ошибка, что данная функция не найдена, так как находиться внутри функции test_function
