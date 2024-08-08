import itertools
from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Цвет остался прежним")

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print("Число сторон осталось прежним")

    def __is_valid_color(self, r: int, g: int, b: int):
        return r <= 255 & r > 0 & g <= 255 & g > 0 & b <= 255 & b > 0

    def __is_valid_sides(self, *sides: list[int]):
        return all(sides) > 0 and len(sides) == len(self.__sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1]
        self.__radius = sides[0] / (2 * pi)
        super().__init__(color, sides)

    def get_square(self):
        return pi * (self.__radius) ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(sides, color)
        self.__height = sum(sides) / 2

    def get_square(self):
        return max(self.__sides) * 0, 5 * self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):

        if len(side) != 1:
            list(side)[0] = 1
        super().__init__(color, sides := list(itertools.repeat(side[0], self.sides_count)))
        self.volume = side[0] ** 3

    def get_volume(self):
        return self.volume


circle1 = Circle((200, 200, 100), 10, 7, 8)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
