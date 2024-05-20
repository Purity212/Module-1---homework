cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]

cars_count = 0
for car in cars:
    print(f"Я езжу на автомобиле марки {car}")
    cars_count += 10
    print(cars_count) #вывожу каждый шаг цикла
#или вне цикла: покажет конечное значение cars_count
print(cars_count)

