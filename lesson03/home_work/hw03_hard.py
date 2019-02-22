# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def fraction_numerator(element): ##Парсим дроби, n может принимать только значения 0 или 2
    fract_num = str(element)
    if fract_num.find("/") != -1:
        numerator = int(fract_num[0:fract_num.find("/")])
        return numerator
    elif fract_num.find("/") == -1:
        numerator = int(fract_num)
        return numerator


def fraction_denominator(element):
    fract_den = str(element)
    if fract_den.find("/") != -1: ##Возвращаем только если находим знак дроби, так как целое возвращает первая функция
        denominator = int(fract_den[fract_den.find("/")+1:])
        return denominator
    else:
        return 1

def action_fract(num1, num2, den1, den2, sign):
    if sign == "+":
        den_whole = den1 * den2
        num_whole = num1*den2 + num2*den1
        modulo = abs(num_whole) % den_whole
        if num_whole < 0:
            whole = abs(num_whole) // den_whole * -1
        else:
            whole = abs(num_whole) // den_whole
        if whole == 0:
            return f"{modulo}/{den_whole}"
        elif modulo == 0:
            return f"{whole}"
        else:
            return f"{whole} {modulo}/{den_whole}"
    if sign == "-":
        den_whole = den1 * den2
        num_whole = num1*den2 - num2*den1
        modulo = abs(num_whole) % den_whole
        if num_whole < 0:
            whole = abs(num_whole) // den_whole * -1
        else:
            whole = abs(num_whole) // den_whole
        if whole == 0:
            return f"{modulo}/{den_whole}"
        elif modulo == 0:
            return f"{whole}"
        else:
            return f"{whole} {modulo}/{den_whole}"


print("Программа чувствительна к пробелам, между числами, операторами вычисления обязательно должны быть пробелы")
parser = input("Введите выражение с простыми дробями для вычисления, формата 5/6 + 4/7: ")
parser = parser.split(" ")

num_1 = fraction_numerator(parser[0]) ##Числитель дроби 1
num_2 = fraction_numerator(parser[2]) ##Числитель дроби 2

sign = parser[1]

den_1 = fraction_denominator(parser[0]) ##Знаменатель дроби 1
den_2 = fraction_denominator(parser[2]) ##Знаменатель дроби 2

print(action_fract(num_1, num_2, den_1, den_2, sign))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
