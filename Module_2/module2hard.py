def find_password(num):
    temp = []
    password = []
    for i in range(1, 21):
        for j in range(1, 21):
            if num % (i + j) == 0 and i != j:
                if [j, i] not in temp: #оставляет только уникальные пары
                    temp.append([i, j])
    for char in temp:
        password += char
    return password





for i in range(3,21):
   print(*find_password(i))
   print()

