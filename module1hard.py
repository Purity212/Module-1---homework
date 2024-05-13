grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#список из средних баллов
average_grades = []
for sublist in grades:
    average_grades.append(sum(sublist)/len(sublist))

#переход от множества к списку, чтобы отсортировать
students = list(students)
students.sort()
#переход от списка к кортежу, т.к. в дальнейшем использую его как ключи для словаря (ключи дожны быть неименяемыми объектами)
students = tuple(students)

dictionary = {}
#вспомогательный индекс, сопоставляю упорядоченные имена учеников с их средним баллом
grades_index = 0
for student in students:
    dictionary[student] = average_grades[grades_index]
    grades_index = grades_index + 1
print(dictionary)





