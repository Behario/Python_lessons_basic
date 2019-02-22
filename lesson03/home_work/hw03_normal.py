# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math


def fibonacci_number(n, m):  #Воспользуемся формулой Бине
    fi = (1 + math.sqrt(5)) / 2
    while n <= m:
        f_n = (fi**n -(-fi)**(-n)) / (2 * fi - 1)  # #Число будет иметь мнимую часть, поэтому при вызове нужно пользоваться методом .real
        f_n = round(f_n.real) ## Округляем до целого
        print(f"{f_n}")
        n += 1


n = int(input("Введите стартовый номер элемента последовательности Фибоначчи: "))
m = int(input("Введите последний номер элемента последовательности Фибоначчи: "))


fibonacci_number(n, m)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(len(origin_list)-1, 0, -1):
        for sort in range(i):
            if origin_list[sort] > origin_list[sort+1]:
                temp = origin_list[sort]
                origin_list[sort] = origin_list[sort + 1]
                origin_list[sort + 1] = temp


a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(a)
print(a)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = ["", "A", 6, 8, "b", -25, 0, 13, 42, 75, True, False]


def check(x):
    return bool(x)


def filters(func, arg):
    lis_t = [i for i in arg if func(i)]
    return lis_t


b = filters(check, a)
print(b)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Решаем через вектора, если они попарно равны, то мы нашли параллеллограм


def parallelogram(A, B, C, D):
    A_B = math.sqrt((B["x2"] - A["x1"]) ** 2 + (B["y2"] - A["y1"]) ** 2)
    A_D = math.sqrt((D["x4"] - A["x1"]) ** 2 + (D["y4"] - A["y1"]) ** 2)
    C_D = math.sqrt((D["x4"] - C["x3"]) ** 2 + (D["y4"] - C["y3"]) ** 2)
    B_C = math.sqrt((C["x3"] - B["x2"]) ** 2 + (C["y3"] - B["y2"]) ** 2)
    if A_B == C_D and A_D == B_C:
        return "Да"
    else:
        return "Нет"


A = {"x1": 1, "y1": 3}
B = {"x2": 4, "y2": 7}
C = {"x3": 2, "y3": 8}
D = {"x4": -1, "y4": 4}
print(f"Даны точки {A} {B} {C} {D}, являются ли они вершинами параллелограмма - {parallelogram(A, B, C, D)}")
