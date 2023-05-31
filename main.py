class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        grade_list = []
        sum_grade = []
        for course, grade in self.grades.items():
            grade_list.append(len(grade))
            sum_grade.append(sum(grade))
            self.average = sum(sum_grade) / sum(grade_list)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average < other.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grade_list = []
        sum_grade = []
        for course, grade in self.grades.items():
            grade_list.append(len(grade))
            sum_grade.append(sum(grade))
            self.average = sum(sum_grade) / sum(grade_list)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average}'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average < other.average


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Nik', 'Klian', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_lecturer_1 = Lecturer('Alex', 'Rider')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_1.courses_attached += ['Git']



cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer_1 = Reviewer('Bill', 'Proshka')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Git']


best_student.rate_lec(some_lecturer, 'Python', 10)
best_student.rate_lec(some_lecturer, 'Python', 10)
best_student.rate_lec(some_lecturer, 'Git', 3)
best_student.rate_lec(some_lecturer, 'Git', 5)

some_student.rate_lec(some_lecturer, 'Git', 3)
some_student.rate_lec(some_lecturer_1, 'Python', 10)


some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 3)
some_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Git', 8)


print(best_student.grades)
print(some_lecturer.grades)
print()
print(some_reviewer)
print()
print(some_lecturer)
print()
print(best_student)
print()
print(some_student)
print()
print(some_lecturer > best_student)
print(some_lecturer < best_student)

student_list = [best_student, some_student]
lecturer_list = [some_lecturer, some_lecturer_1]


def average_student(student_list, course):
    sum_all = []
    count_all = 0
    for stud in student_list:
        grades = stud.grades.get(course)
        sum_all.extend(grades)
        count_all += len(grades)
    if count_all > 0:
        average_grade = sum(sum_all) / count_all
        return round(average_grade, 1)
    else:
        return 'Нет оценок для данного курса'


def average_lecturer(lecturer_list, course):
    sum_all = []
    count_all = 0
    for lec in lecturer_list:
        grades = lec.grades.get(course)
        sum_all.extend(grades)
        count_all += len(grades)
    if count_all > 0:
        average_grade = sum(sum_all) / count_all
        return round(average_grade, 1)
    else:
        return 'Нет оценок для данного курса'

print()
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {average_student(student_list, 'Python')}")
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {average_lecturer(lecturer_list, 'Python')}")

