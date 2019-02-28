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
        path_main = os.getcwd()  # Определяем текущую директорию и применяем ее для создания новой папки:
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


