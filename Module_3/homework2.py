#1 - Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)



# print_params(42, "Привет",  False, 4234)   --- вызов функции с кол-вом аргументов > 3
                                             # приводит к ошибке
print_params()

print_params(42, "Привет",  False)

#2 - Распаковка параметров

values_list = [True, 4.15, 50]
values_dict = {'a' : False, 'b' : 'строчка', 'c' : 128}

print_params(*values_list,)
print_params(**values_dict)

#3 - Распаковка + отдельные параметры
values_list_2 = [1,True]
print_params(*values_list_2, 45)