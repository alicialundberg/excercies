class Car():

    def __init__(self, driver, color, doors):
        self.driver = driver
        self.color = color
        self.doors = doors

    def getDriver(self):
        return self.driver

    def getColor(self):
        return self.color

    def getDoors(self):
        return self.doors

    def __str__(self):
        return self.driver + " is the driver. The cars color is " + self.color + " and have " + str(self.doors) + " doors."
