
class Program():

    def __init__(self, name, points, courseList, students, teacherObj=None):
        self.name = name # string
        self.points = points # int
        self.courseList = courseList # list

        self.__admin = teacherObj # underscore * 2 = privat, går ej att förändra

        self.studentList = list() # list
        self.studentList = students

    def setAdmin(self, teacherObj):
        self.__admin = teacherObj


    def getStudents(self):
        return self.studentList

    def addStudent(self, studentObj):
        self.studentList.append(studentObj)


    def removeStudent(self, studentObj):
        self.studentList.remove(studentObj)

    def __str__(self):
        s = self.name + " " + str(self.points) + " total HP \n"
        s += "Lärare: " + self.__admin.name + "\n"

        for c in self.courseList:
            s += c.name + "-" + str(c.points) + " \n"

        s+= str(len(self.studentList)) + " number of students."

        return s