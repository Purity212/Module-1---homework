def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        inner_function() #внутри test_function

inner_function() #вне test_function - не видит функцию т.к. она определена в локальной области видимости test_function

