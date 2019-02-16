_author__ = 'Косцов Антон Сергеевич'
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
#Решение
import math
a = [9, 6, 25, -9, 123, 36, -36]
print(f"Список а имеет вид - {a}")
b = []
print(f"Список б пока пустой {b}")

for i in a:
     if i >=0 and i % math.sqrt(i) == 0:
         b.append(math.sqrt(i))

print(f"Список б имеет вид {b}")
         

#Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
#Решение

date_num = "12.05.2018"
print(f"Наша дата имеет вид {date_num}")
date_num = date_num.split(".")
date_day = {"12":"двенадцатое"}
date_month = {"05":"мая"}

for key1 in date_day:
     if date_num[0] == key1:
          date_num[0] = date_day[key1]

for key2 in date_month:
     if date_num[1] == key2:
          date_num[1] = date_month[key2]

print("Мы преобразовывем ее в {0} {1} {2} года".format(date_num[0], date_num[1], date_num[2]))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
