from student import Student
from course import Course
from program import Program
from teacher import Teacher
from school import School


s1 = Student("Alicia", "allu16", 15)
s2 = Student("Joakim", "joth16", 105)
sList = [s1, s2, Student("alicia", "allu16", 2)]

t = Teacher("Hasse", "haha@hej.com")

c = Course("Webbutveckling", "ME1572", 15, t)

p = Program("Interaktion med webbteknologier", 180, [c], sList, t)

u = School("Blekinge tekniska högskola", "Karlskrona", str(Program[p]))

p.addStudent(Student("Nellie", "Nelu16", 15))

ss = p.getStudents()

print(u)


def inputSchool():
    n = input("School name: ")
    c = input("School city: ")

    sc = School(n, c)

def inputStudent():
    n = input("Student name: ")
    a = n.split()
    a = ' '.join(w[0:2].lower() for w in a)
    s = Student(n, a)



# Om man vill förändra ett attribut kan man göra på följande sätt
# s1.name = "Lisa" #alternativ 1
# sList[1].name = "Alicia"  #alternativ 2
# p.studentList[0].name = "Alizia" # alternativ 3
# print(s1)
#print(p.studentList[1]

