# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
# Решение

def math_round(integer, accuracy):
    if integer % 1 > 0:
        a_fraction = integer % 1
        a_fraction = a_fraction * 10 ** accuracy
        if a_fraction % 1 < 0.5:
            a_fraction = a_fraction // 1
            integer = integer // 1 + a_fraction / 10 ** accuracy
            if integer == int(integer): #Если число равно, условно, 3.0, то только так я смог избавиться от ненужного 0 после запятой
                integer = int(integer)
                return integer
            return integer
        elif a_fraction % 1 >= 0.5:
            a_fraction = a_fraction // 1
            a_fraction = a_fraction + 1
            integer = integer // 1 + a_fraction / 10 ** accuracy
            if integer == int(integer):
                integer = int(integer)
                return integer
            return integer


print(math_round(2.1234567, 5))
print(math_round(2.1999967, 5))
print(math_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
# Решение (считает сумму первых трех и последних трех цифр и сравнивает, если равны - возвращает True, если нет - False
# Если в билете нет шести цифр - False

def lucky_shot(ticket_numbers):
    ticket_numbers = str(ticket_numbers)
    if len(ticket_numbers) != 6:
        return False
    i = 0
    sum_0 = 0
    while i < len(ticket_numbers)/2:
        sum_0 = sum_0 + int(ticket_numbers[i])
        i += 1
    n = 3
    sum_1 = 0
    while n != len(ticket_numbers):
        sum_1 = sum_1 + int(ticket_numbers[n])
        n += 1
    if sum_0 == sum_1:
        return True
    elif sum_0 != sum_1:
        return False


print(lucky_shot(123006))
print(lucky_shot(12321))
print(lucky_shot(436751))