class Teacher:

    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        print(f"Welcome to class! I'm your teacher. My name is {self.full_name}")


class ScienceTeacher(Teacher):

    def welcome_students(self):
        print("Science is amazing.")
        #Teacher.welcome_students(self)
        super().welcome_students()

my_science_teacher = ScienceTeacher("Amir", "5129203")
my_science_teacher.welcome_students()