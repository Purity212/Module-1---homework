class House:
    def __init__(self, number_of_floors):
        self.num_of_floors = number_of_floors

    def set_new_number_of_floors(self, floors):
        self.num_of_floors = floors
        print("Теперь у дома {self.num_of_floors} этажей")



dom = House(16)
dom.set_new_number_of_floors(5)
