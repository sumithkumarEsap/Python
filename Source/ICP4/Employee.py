class Employee:
    empCount = 0
    tsal = 0
    avgsal = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.tsal += int(salary)

    def average_salary(self):
        print("average salary of all employees is  %d" % (Employee.tsal / Employee.empCount))

    def explain_interitance(self):
        print("this is output from parent class")


class Fulltime_Employee(Employee):
    def another_method(self):
        print("this is outpur from child class")


emp1 = Employee("sumith", "r1 ", "10", "random1")
emp2 = Employee("vishal", "r2", "20", "random2")
emp3 = Employee("kiran rao", "r3", "20", "random3")
emp4 = Employee("kranti", "r4", "30", "random4")
emp5 = Fulltime_Employee("vinay", "r5", "50", "random5")
print("Total Employee %d" % Employee.empCount)
# calling average function to get the average salary
emp1.average_salary()

emp5.explain_interitance()
emp5.another_method()