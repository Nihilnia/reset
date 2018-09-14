from time import sleep

class Workers():
    default = "IT's a default Text!"
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def ShowInfos(self):
        print("Worker name: {}\nSalary: {}\nDepartment: {}".format(self.name, self.salary, self.department))


class Managers(Workers):
    def ChangeSalary(self, newSalary):
        self.salary = newSalary

manager01 = Managers(name = "nihil", salary = 3000, department = "R&D")
manager01.ShowInfos()
#Changing the salary
manager01.ChangeSalary(newSalary = 5000)
print("Salary changing with {}...".format(manager01.salary))
sleep(2)
manager01.ShowInfos()
print(manager01.default)