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


content()

while True:

    run = input("Давайте поработаем? (Y/N): ")

    if run.lower() == "y":
        message()
        question = input("Что желаете сделать? ")
        if question == "1":
            name_dir = input("Введите название папки для перехода: ")
            hw5.move(name_dir)
            input(f"Сейчас вы находитесь в {os.getcwd()}")

        elif question == "2":
            print(f"Вы находитесь в папке {name_dir}")
            print(hw5.show_dc())

        elif question == "3":
            a = os.path.dirname(os.path.realpath(__file__))  # Нашел интересный код - возвращает всегда путь к директории, из которой запускают рабочий файл
            os.chdir(a)
            name_del = input("Введите название папки, которую желаете удалить: ")
            hw5.delete(name_del)

        elif question == "4":
            a = os.path.dirname(os.path.realpath(__file__))
            os.chdir(a)
            name_create = input("Введите название папки, которую желаете создать: ")
            hw5.create(name_create)

        else:
            print("Команда введена неверно")
            pass

    elif run.lower() == "n":
        print("Работа программы окончена")
        break

    else:
        print("Я не могу обработать команду")











