
class Course():

    def __init__(self, name, code, points, teacherObj=None):
        self.name = name
        self.code = code
        self.points = points

        self.courseAdmin = teacherObj


    def __str__(self):
        s = self.name + "\n" + self.code + " " + str(self.points) + "HP."

        if not self.courseAdmin == None:
            s += self.courseAdmin.name


        return s


