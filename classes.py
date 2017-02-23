
class Employee(object):
    raiseAmount = .23
    numofemployees = 201
    hoursWorked = 40

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def printname(self):
        return self.first + ' ' +self.last

    def weeklyPay(self):
        return(self.hoursWorked * self.pay)

    def weeklyPayRaise(self):
        return(self.hoursWorked * self.pay * self.raiseAmount)

    @classmethod
    def setRaiseAmount(cls,amount):
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls,empStr):
        first,last,pay = empStr.split('-')
        return cls(first,last,float(pay))

class Devloper(Employee):
    def __init__(self,first,last,pay,language):
        super(Devloper,self).__init__(first,last,pay)
        self.language = language

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super(Devloper,self).__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addemp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rmemp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def printemps(self,emp):
        for emp in self.employees:
            print "--->" + emp.printname()

dev1 = Devloper('Frank','Chipmonk',12,"python")
dev2 = Devloper('kitt','katt',13,"swift")
man1 = Manager('Tom','Lee',15,[dev1])
man1.addEmp(dev2)
man1.printEmp()
man1.rmemp(dev1)
