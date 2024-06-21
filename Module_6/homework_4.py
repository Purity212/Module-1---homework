class Building:
    total = 0

    def __init__(self):
        Building.total += 1

    def __str__(self):
        return f'Строение № {self.total}'


for i in range(40):
    b = Building()
    print(b)

