
class Employee:
    raise_amt = 1.05

    def __init__(self, f_name, s_name, pay):
        self.f_name = f_name
        self.s_name = s_name
        self.pay = pay

    def full_name(self):
        return "Employee full name is {} {}".format(self.f_name, self.s_name)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    def __add__(self,other):
        return self.pay+ other.pay


class Developer(Employee):

    def __init__(self,f_name,s_name,pay,prog_lang):
        super().__init__(f_name,s_name,pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return "{} pay is {} ".format(self.f_name, self.pay)

    def __str__(self):
        return "{} {} programing language is {}".format(self.f_name, self.s_name, self.prog_lang)



class Manager(Employee):
    def __init__(self,f_name,s_name,pay,employees = None):
        super().__init__(f_name, s_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            return self.employees

    def print_emp(self):
        for emp in self.employees:
            print (emp.full_name())

    def __add__(self,other):
        return self.pay+ other.pay


dev1 = Developer("navaneetha","sekar",30000,"python")
dev2 = Developer("nandhini","prasanna",30000,"java")
mgr1 = Manager("prasanna","sekar",50000,[dev1])

print(dev1 + dev2)

#print(dev2.__str__())
#print(dev1.__repr__())
#print(dev1.__str__())

