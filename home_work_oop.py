class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                grad = list(lecturer.grades.values())[0]  #
                lecturer.av_grad = round(sum(grad) / len(grad), 1)
            else:
                lecturer.grades[course] = [grade]
                grad = list(lecturer.grades.values())[0]
                lecturer.av_grad = round(sum(grad) / len(grad), 1)
        else:
            return 'Ошибка'

    # Решение задачи 3.1:
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grad}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"

    # Решение задачи 4:
    def __sub__(self, other):
        return self.av_grad - other.av_grad

    def __eq__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError('Оператор справа должен сходить в класс Student')
        sc = ither if isinstance(other, int) else other.av_grad
        return self.av_grad == sc


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Решение задачи 3.1:
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grad}\n"

    # Решение задачи 4:
    def __sub__(self, other):
        return self.av_grad - other.av_grad


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                grad = list(student.grades.values())[0]
                student.av_grad = round(sum(grad) / len(grad), 1)
            else:
                student.grades[course] = [grade]
                grad = list(student.grades.values())[0]
                student.av_grad = round(sum(grad) / len(grad), 1)
        else:
            return 'Ошибка'

    # Решение задачи 3.1:
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Java']

student_2 = Student('Vy', 'Sky', 'girl')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['PHP', 'JavaScript']

student_3 = Student('Vod', 'Ka', 'girl')
student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Java']
student_3.finished_courses += ['PHP']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Abby', 'Tyu')
lecturer_2.courses_attached += ['Python', 'PHP']

reviewer_1 = Reviewer('Ivan', 'Ivanov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Rustam', 'Tot')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

student_1.rate_lection(lecturer_1, 'Python', 3)
student_1.rate_lection(lecturer_1, 'Python', 8)
student_1.rate_lection(lecturer_1, 'Python', 9)

student_2.rate_lection(lecturer_2, 'Python', 5)
student_2.rate_lection(lecturer_2, 'Python', 7)
student_2.rate_lection(lecturer_2, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 2)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Java', 1)
reviewer_1.rate_hw(student_2, 'Java', 2)

reviewer_1.rate_hw(student_3, 'Python', 5)
reviewer_1.rate_hw(student_3, 'Python', 3)
reviewer_1.rate_hw(student_3, 'Python', 4)

reviewer_2.rate_hw(student_3, 'Java', 8)
reviewer_2.rate_hw(student_3, 'Java', 8)
reviewer_2.rate_hw(student_3, 'Java', 7)

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

print(student_1)
print(student_2)


# Решение задачи 3.2 (сравнение):
# Если некорректно, то в конце показал вычитание средих баллов у студентов и лекторов.
def print_who_more(pers_1, pers_2):
    if pers_1.av_grad > pers_2.av_grad:
        print(f"У {pers_1.name} {pers_1.surname} больше баллов чем у {pers_2.name} {pers_2.surname}")
    elif pers_1.av_grad == pers_2.av_grad:
        print(f"У {pers_1.name} {pers_1.surname} и у {pers_2.name} {pers_2.surname} одинаковое количество баллов")
    else:
        print(f"У {pers_1.name} {pers_1.surname} меньше баллов чем у {pers_2.name} {pers_2.surname}")


print_who_more(student_1, student_2)
print_who_more(lecturer_1, lecturer_2)


def print_diff_points(pers_1, pers_2):
    if pers_1.av_grad > pers_2.av_grad:
        print(
            f"{pers_1.name} {pers_1.surname} имеет на {int(pers_1.av_grad - pers_2.av_grad)} больше балла(ов) чем {pers_2.name} {pers_2.surname}")
    elif pers_1.av_grad == pers_2.av_grad:
        print(f"У {pers_1.name} {pers_1.surname} и у {pers_2.name} {pers_2.surname} одинаковое количество баллов")
    else:
        print(
            f"{pers_1.name} {pers_1.surname} имеет на {int(pers_2.av_grad - pers_1.av_grad)} меньше балла(ов) чем {pers_2.name} {pers_2.surname}")


print_diff_points(student_1, student_2)
print_diff_points(lecturer_1, lecturer_2)


# Решение задачи 4
def avg_points_stud(persons, course):
    sum_points = 0
    for person in persons:
        if course in person.courses_in_progress:
            if sum_points > 0:
                sum_points += person.av_grad
            else:
                sum_points = person.av_grad
        else:
            pass
    return f'На курсе {course} у студентов среднее количество баллов составляет: {round(sum_points / len(persons), 1)}'


def avg_points_lect(persons, course):
    sum_points = 0
    for person in persons:
        if course in person.courses_attached:
            if sum_points > 0:
                sum_points += person.av_grad
            else:
                sum_points = person.av_grad
        else:
            pass

    return f'На курсе {course} у лекторов среднее количество баллов составляет: {round(sum_points / len(persons), 1)}'


print(avg_points_stud([student_1, student_2], "Python"))
print(avg_points_lect([lecturer_1, lecturer_2], "Python"))
print(avg_points_stud([student_1, student_2, student_3], "Java"))

# Решение задачи 3.2 (сравнение):
print(student_1 - student_2)
print(lecturer_1 - lecturer_2)

print(student_1.av_grad)
print(student_2.av_grad)
print(student_1 == student_2)