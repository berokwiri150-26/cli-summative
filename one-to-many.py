# # student => teacher

# class Teacher:
#          def __init__(self, name):
#             self.name = name
#             self._students = []

#             def students(self):
#                 return list self._students

#     def students(self):
#         return list(self._students)
#         # return [student for student in Student.all_students if student.teacher == self]
    
#     def add_student(self, new_student):
#         if not isinstance(new_student, Student):
#             raise TypeError("Must be of student class")
#         new_student.teacher = self
#         if new_student not in self._students:
#             self._students.append(new_student)

# class Student:

#     all_students = []
#     def __init__(self, name):
#         self.name = name
#         self._teacher = None

#     @property
#     def teacher(self):
#         return self._teacher
    
#     @teacher.setter
#     def teacher(self, new_teacher):
#         if not isinstance(new_teacher, Teacher):
#             raise TypeError("Must be of class Teacher")
#         self._teacher = new_teacher


# student1 = Student("Bett")
# student2 = Student("Beatrice")
# student3 = Student("Sister")
# student4 = Student("Bettina")
# student5 = Student("Bernd")

# titus = Teacher("Titus")
# joseph = Teacher("Joseph")

# titus.add_student(student3)
# titus.add_student(student5)

# joseph.add_student(student1)
# joseph.add_student(student2)
# joseph.add_student(student4)

# student1.teacher = joseph 
# student2.teacher = joseph
# student3.teacher = titus
# student4.teacher = titus
# student5.teacher = joseph

# print(titus.students())

# teacher1 = Teacher("Titus")

# student1.teacher = teacher1
# print(student1.teacher)

# print(Student.all_students)



# student => teacher

class Student:
    all_students = []

    def __init__(self, name):
        self.name = name
        self._teacher = None
        Student.all_students.append(self)

    def __repr__(self):
        return f"Student({self.name!r})"

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, new_teacher):
        if not isinstance(new_teacher, Teacher):
            raise TypeError("Must be of class Teacher")
        if self._teacher is new_teacher:
            return
        if self._teacher is not None:
            try:
                self._teacher._students.remove(self)
            except ValueError:
                pass
        self._teacher = new_teacher
        if self not in new_teacher._students:
            new_teacher._students.append(self)


class Teacher:
    def __init__(self, name):
        self.name = name
        self._students = []

    def students(self):
        return list(self._students)

    def add_student(self, new_student):
        if not isinstance(new_student, Student):
            raise TypeError("Must be of Student class")
        new_student.teacher = self



student1 = Student("Bett")
student2 = Student("Beatrice")
student3 = Student("Sister")
student4 = Student("Bettina")
student5 = Student("Bernd")

titus = Teacher("Titus")
joseph = Teacher("Joseph")

titus.add_student(student3)
titus.add_student(student5)

joseph.add_student(student1)
joseph.add_student(student2)
joseph.add_student(student4)

print([student.name for student in titus.students()])
print([student.name for student in Student.all_students])