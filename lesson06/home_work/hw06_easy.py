# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt


class Rectangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = 0
        self.bc = 0
        self.ac = 0
        self.p = 0
        self.h = 0

    def perimeter(self):
        self.ab = sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        self.bc = sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)
        self.ac = sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)
        return round(self.ab + self.bc + self.ac, 3)

    def height(self):
        self.p = (self.ab + self.bc + self.ac) * 1 / 2
        self.h = 2 * sqrt(self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ac)) / self.ab
        return round(self.h, 2)

    def square(self):
        square = (self.ab * self.h) / 2
        return square


rect1 = Rectangle([1, 3], [8, 7], [2, 9])

print(f"Периметр равен: {rect1.perimeter()}")
print(f"Высота равна: {rect1.height()}")
print(f"Площадь треугольника равна: {rect1.square()}")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

