
class Employee:
    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, name, age, email, pay):
        self.name=name
        self.age = age
        self.email= email
        self.pay = pay
        Employee.num_of_emp += 1

    def name_age(self):
        return "{} age is {}".format(self.name, self.age)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, name, age, email, pay, prog_lang):
        super().__init__(name,age,email,pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, name, age, email, pay, employees = None):
        super().__init__(name, age, email, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            return self.employees

    def del_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print (emp.name_age())


dev_1 = Developer("prasanna",25,"myidprasanna@gmail.com",25000,"python")
dev_2 = Developer("kannan",30,"navaneethn55@gmail.com", 30000,"java")

mgr_1 = Manager("ragu",35,"ragu@gmail.com",50000,[dev_1])

print(mgr_1.add_emp())

dev_1.__repr__()



