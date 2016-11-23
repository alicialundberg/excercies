from student import Student
from course import Course
from program import Program
from teacher import Teacher
from school import School


def inputSchool():
    n = input("School name: ")
    c = input("School city: ")

    sc = School(n, c)

def inputStudent():
    n = input("Student name: ")
    a = n.split()
    a = ' '.join(w[0:2].lower() for w in a)

    s = Student(n, a)

# code is under construction, more will be added!



