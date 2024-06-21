class Building:
    def __init__(self, num_of_floors, building_type):
        self.num_of_floors = num_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return self.building_type == other.building_type and self.num_of_floors == other.num_of_floors



b_1 = Building(16, 'Хрущевка')
b_2 = Building(1, 'Дача')

print(b_1 == b_2)