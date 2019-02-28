# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy as hw5
import os


def message():
    print("Приветствую Вас! Данная программа позволяет работать с папками текущей директории\n"
              "Команда №1 - введите 1, чтобы перейти в папку\n"
              "Команда №2 - введите 2, чтобы просмотреть содержимое\n"
              "Команда №3 - введите 3, чтобы удалить папку\n"
              "Команда №4 - введите 4, чтобы создать папку\n")


def content():
    print("В каталоге содержатся следующие папки: \n"  
          f"{hw5.show_f()}")


question = ""

while True:

    run = input("Давайте поработаем? (Y/N): ")

    if run.lower() == "y":
        message()
        content()
        question = input("Что желаете сделать? ")
        origin = os.getcwd()
        if question == "1":
            name_dir = input("Введите название папки для перехода: ")
            hw5.move(name_dir)
            input(f"Сейчас вы находитесь в {os.getcwd()}")
            ask = input("Желаете посмотреть содержимое? Y:да / N:нет ")

            if ask.lower() == "y":
                print(hw5.show_dc())

            elif ask.lower() == "n":
                print(f"Вы отказались посмотреть на содержимое папки {name_dir}")
            # Пошел на маленькую хитрость, после окончания блока 1 мы возвращаемся в исходную директорию
            hw5.move(origin)  # Создание и удаление файлов мы производим из главной директории
            # Так же по желанию пользователя, он может из главной директории посмотреть содержание любой папки
        elif question == "2":
            name_dir = input("Введите название файла, содержание которого вы желаете посмотреть: ")
            print(hw5.show_d())

        elif question == "3":
            name_dir = input("Введите название папки, которую желаете удалить: ")
            hw5.delete(name_dir)

        elif question == "4":
            name_dir = input("Введите название папки, которую желаете создать: ")
            hw5.create(name_dir)

        else:
            print("Команда введена неверно")
            pass

    elif run.lower() == "n":
        print("Работа программы окончена")
        break

    else:
        print("Я не могу обработать команду")











