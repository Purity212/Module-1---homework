#1
text = "I am Habib Nurmagomedov"
print("Часть предложения:", text.split(" ")[3])
# или
print("Часть предложения:", text[5:])
#2
text = "норма"
print("В обратном порядке:", "норма"[::-1])
#3
text = "кенгуру"
middle_index = len(text)/2 + 1
print("Равные части:", text[int(middle_index):] + text[:int(middle_index)])
#4
text = "нейропрограммирование"
print(text[::2], " ", text[1::2])
#5
text = "нейропластичность"
print(text[-2:0:-1])