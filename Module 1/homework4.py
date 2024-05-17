# Immutable - tuple
immutable_var = tuple([10, "кортеж", False, 3.5, [1, 2]])
print("Кортеж:", immutable_var)

# immutable_var[2] = True
# ошибка! - кортеж является неизменяемой структурой данных

# однако, я могу повлиять на изменяемые объекты внутри него (здесь: лист)
immutable_var[4][0] = 10
print("Заменил элемент списка - элемента кортежа", immutable_var)

# Mutable - list
mutable_var = [0.1, "лист", True, 3, [1, 2]]
print("Список:", mutable_var)
mutable_var = [5, 3.6, False]
print("Измененный список:", mutable_var)



