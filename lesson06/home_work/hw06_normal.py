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


class Teacher:
    def __init__(self, fio, lesson, classes_room):
        self.fio = fio
        self.lesson = lesson
        self.classes_room = classes_room


class Pupil:
    def __init__(self, fio,  father, mother, classroom):
        self.fio = fio
        self.father = father
        self.mother = mother
        self.classroom = classroom

    @property
    def get_pupil_parents(self):
        return f"Родители ученика {self.fio}: отец - {self.father}, мать - {self.mother}"


class School:
    def __init__(self, num, city, sch_rooms):
        self.num = num
        self.city = city
        self.sch_rooms = sch_rooms

    @property
    def get_all_rooms(self):
        return self.sch_rooms


def get_pupil_name(name):
    for i in range(len(pupils)):
        if pupils[i].fio == name:
            return pupils[i].get_pupil_parents
        elif pupils[i].fio != name:
            continue
    return "У нас нет такого ученика"


def get_pupils(class_room):
    pupils_list = []
    for i in range(len(pupils)):
        if pupils[i].classroom == class_room:
            pupils_list.append(pupils[i].fio)
        else:
            continue
    pupils_list = ", ".join(pupils_list)
    return f"В классе {class_room} есть следующие ученики:\n" \
        f"{pupils_list}"


def get_subjects(name):
    teach = []
    subj = []
    room = ""
    for i in range(len(pupils)):
        if pupils[i].fio == name:
            room += pupils[i].classroom
            for k in range(len(teachers)):
                if pupils[i].classroom in teachers[k].classes_room:
                    subj.append(teachers[k].lesson)
                    teach.append(teachers[k].fio)
        elif pupils[i].fio == name:
            continue
    teach = ", ".join(teach)
    subj = ", ".join(subj)
    return f"Ученик: {name} --- Класс: {room} --- " \
        f"Проподаватели: {teach} --- Предметы: {subj}"


def get_teachers(classroom):
    teach_class = []
    for i in range(len(teachers)):
        if classroom in teachers[i].classes_room:
            teach_class.append(teachers[i].fio)
        elif classroom not in teachers[i].classes_room:
            continue
    teach_class = ", ".join(teach_class)
    return f"В классе {classroom} преподают учителя: {teach_class}"


rooms_a = [str(i+1)+" А" for i in range(10)]
rooms_b = [str(i+1)+" Б" for i in range(10)]
school_rooms = rooms_a + rooms_b

school = School("115", "Минск", school_rooms)

teachers = [Teacher("Апимахович А. А.", "Русский язык", ["5 А", "7 А"]),
            Teacher("Сапковский А. О.", "Математика", ["5 Б", "9 А"]),
            Teacher("Руанов В. Ю.", "Физика", ["8 А", "7 А"])]


pupils = [Pupil("Косцов А. С.", "Косцов С. Н.", "Косцова Л. К.", "7 А"),
          Pupil("Косцов С. С.", "Косцов С. Н.", "Косцова Л. К.", "8 А"),
          Pupil("Добрин Н. Н.", "Добрин А. В.", "Добрина В. С.", "7 А"),
          Pupil("Варатов С. К.", "Варатов В. Ю.", "Варатова Е. С.", "9 А")]

name_pupil = input("Введите фамилию ученика в формате - Фамилия И. О.: ")
print(get_pupil_name(name_pupil))
print("----------------------------")
print(f"В школе есть следующие классы:\n{school.get_all_rooms}")
print("----------------------------")
name_classroom = input("Введите название класса для получения списка учеников: ")
print(get_pupils(name_classroom))
print("----------------------------")
name_pupil1 = input("Введите имя ученика, чтобы узнать, в каком он классе: ")
print(get_subjects(name_pupil1))
print("----------------------------")
name_class = input("Введите название класса, чтобы узнать всех преподавателей в нем: ")
print(get_teachers(name_class))