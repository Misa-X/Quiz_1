class Employee:
    def __init__(self, id=" ", name=" ", position=" ", salary=0):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getSalary(self):
        return self.salary

    def __str__(self):
        string = "[ID= "+ self.getId() + ", Name= "+ self.getName() + ", Position= "+ self.getPosition()+ ", Salary= "+ str(self.getSalary()) +"]"
        return string

employee1 = Employee("S0001", "Gary", "Staff", 4500000)
employee2 =  Employee("S0002", "James", "Staff", 5000000)
employee3 = Employee("S0003", "Judith", "Manager", 10700000)
employee4 =  Employee("S0004", "Yuli", "Officer", 8500000)
print("Employee 1 :", employee1.__str__())
print("Employee 2 :", employee2.__str__())
print("Employee 3 :", employee3.__str__())
print("Employee 4 :", employee4.__str__())


