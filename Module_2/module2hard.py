def find_password(num):
    password = []
    for i in range(1, 21):
        for j in range(1, 21):
            if num % (i + j) == 0 and i != j:
                if [j, i] not in password: #оставляет только уникальные пары
                    password.append([i, j])
    for char in password:
        print(*char, end=' ')
    print()


for i in range(3,21):
    find_password(i)


