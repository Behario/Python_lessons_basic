import os
import shutil
import sys
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir():
    i = 1
    while i < 10:
        path_main = os.getcwd() # Определяем текущую директорию и применяем ее для создания новой папки:
        path = f"{path_main}/dir_{i}"
        try:
            os.mkdir(path)
        except OSError:
            print(f"Создание директории {path} не удалось")
            i += 1
        else:
            i += 1


def delete_dir():
    i = 1
    while i < 10:
        path_main = os.getcwd()  # Определяем текущую директорию и применяем ее для удаления ранее созданных папок:
        path = f"{path_main}/dir_{i}"
        try:
            os.rmdir(path)
        except OSError:
            print(f"Удалить директорию {path} не удалось")
            i += 1
        else:
            i += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dir():
    path = os.getcwd()
    return [d for d in os.listdir(path) if os.path.isdir(d)]


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy():
    file_name = sys.argv[0]
    name_destination = file_name.split("/")
    name_destination = name_destination[-1]
    shutil.copyfile(file_name, f"{name_destination}.copy")

# ---------------------------------------------------------------------------------- #
# Скрипты для задания Normal


def show_f():  # Показывает содержимое главного каталога (только папки)
    path = os.getcwd()
    return [d for d in os.listdir(path) if os.path.isdir(d)]


def show_dc():  # Показывает содержимое из текущей папки
    path = os.getcwd()
    return os.listdir(path)


def move(req_dir):  # Перейти в новую папку
    path = f"{req_dir}"
    try:
        os.chdir(path)
    except NameError:
        print("Переход невозможен")
    else:
        print(f"Папка {req_dir} возможна для перехода")


def delete(req_dir):  # Удалить папку
    path = f"{req_dir}"
    try:
        os.rmdir(path)
    except OSError:
        print(f"Удалить папку {path} не удалось")
    else:
        print("Удаление прошло успешно")


def create(req_dir):  # Создать папку
    path = f"{req_dir}"
    try:
        os.mkdir(path)
    except OSError:
        print(f"Создание папки {path} не удалось")
    else:
        print("Папка была успешно создана")


