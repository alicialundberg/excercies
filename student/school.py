class School():

    def __init__(self, name, city, programList):
        self.name = name
        self.city = city

        self.programList = programList

    def getProgram(self):
        return self.programList

    def addProgram(self, programList):
        self.programList.append(programList)

    def removeProgram(self, programList):
        self.programList.remove(programList)

    def __str__(self):
        return self.name + " located in " + self.city + " have following programs and courses avaiable: \n" + self.programList
