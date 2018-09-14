from time import sleep

class students():

    def __init__(self, name = "Unknown", surname = "Unknown", number = 0000):
        self.name = name
        self.surname = surname
        self.number = number

    def showInfos(self):
        print("""
        Student number: {}
        Name: {}
        Surname: {}
        """.format(self.number, self.name, self.surname))

    def changeInfos(self, newName, newSurname, newNumber):
        self.name = newName
        self.surname = newSurname
        self.number = newNumber


student0001 = students(name = "okan", surname = "topal", number = 1)
student0001.showInfos()
print("Infos changing..")
sleep(2)
student0001.changeInfos(newName = "nihil!", newSurname = "Unknown", newNumber = 9999)
student0001.showInfos()