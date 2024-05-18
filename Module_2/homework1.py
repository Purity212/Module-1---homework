#3
x = 100
if x < 0 and x != 0:
    print("Меньше 0")
else:
    print("Больше 0")
#4
a, b = 5, 10
if a > b:
    print("a > b")
if a > b and a > 0:
    print("успех")
if (a > b) and (a > 0 or b < 1000):
    print("успех")
if 5 < b and b > 10:
    print("успех")
#6
if "34" > "123":
    print("Строки - успех")
if "123" > "12":
    print("Строки - успех")
if [1,2] > [1,1]:
    print("Списки - успех")
#7
#if "6" > 5:
   #if [5, 6] > 5:
    #   print("Разные типы - успех")
#но
if "5" != 5:
    print("Но, успех")