# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, surname, n_p):
        self.surname = surname
        self.n_p = n_p


class Teacher(People):
    def __init__(self, surname, n_p, class_room, subject):
        People. __init__(self, surname, n_p)
        self._class_room = class_room
        self._subject = subject


class Pupil(People):
    def __init__(self, surname, n_p, class_room, subjects):
        People. __init__(self, surname, n_p)
        self._class_room = {"class_num": int(class_room.split()[0]),
                            "class_char": class_room.split()[1]}
        self._subjects = subjects

    @property
    def get_room(self):
        return f"{self.get_name} \n" \
            f"{self._class_room['class_num']} {self._class_room['class_char']}"

    @property
    def get_name(self):
        return self.surname + " " + self.n_p


pupil1 = Pupil("Косцов", "А. С.", "7 A", ["математика", "русский", "география"])
pupil2 = Pupil("Стасенко", "А. В.", "3 А", ["черчение", "русский", "география"])
pupil2 = Pupil("Валерьянка", "Ю. А.", "5 б", ["математика", "русский", "география"])

teacher1 = Teacher("Касяьнов", "А. В.")

print(f"{pupil1.get_room}")