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


class Trapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)  # Левая боковая сторона
        self.bc = sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)  # Верхнее основание трапеции
        self.cd = sqrt((self.d[0] - self.c[0]) ** 2 + (self.d[1] - self.c[1]) ** 2)  # Правая боковая сторона
        self.ad = sqrt((self.d[0] - self.a[0]) ** 2 + (self.d[1] - self.a[1]) ** 2)  # Нижнее основание трапеции
        self.d1 = sqrt(
            self.cd ** 2 + (self.bc * self.ad) - self.ad * (self.cd ** 2 - self.ab ** 2) / (self.ad - self.bc))  # Диагональ 1
        self.d2 = sqrt(
            self.ab ** 2 + (self.bc * self.ad) - self.ad * (self.ab ** 2 - self.cd ** 2) / (self.ad - self.bc))  # Диагональ 1
        self.h = None

    def check_trapezium(self):  # Признак диагоналей
        if self.d1 ** 2 + self.d2 ** 2 \
                == 2 * self.ad * self.bc + self.ab ** 2 + self.cd ** 2:  # Доп проверка, а вдруг это вообще не трапеция!
            if self.d1 == self.d2:
                print(f"Это равнобедренная трапеция."
                         f" Диагонали равны: диагональ 1 = {round(self.d1, 2)}"
                         f" и диагональ 2 = {round(self.d2, 2)}")
            else:
                print(f"Это неравнобедренная трапеция."
                         f" Диагонали не равны: диагональ 1 = {round(self.d1, 2)}"
                         f" и диагональ 2 = {round(self.d2, 2)}")
        else:
            print("Это не трапеция")

    def sq(self):
        try:
            self.h = sqrt(
                self.ab - (((self.ad - self.bc) ** 2 + self.ab ** 2 - self.cd ** 2) / 2 * (self.ad - self.bc)) ** 2)
            s = (self.ad + self.bc) * self.h / 2
        except ValueError:
            print("Похоже что - то пошло не так, но мы скоро выясним!")
        else:
            print(f"Плащадь трапеции равна: {s}")


trapezium1 = Trapezium([-2, -2], [-3, 1], [7, 7], [3, 1])

trapezium1.check_trapezium()
trapezium1.sq()