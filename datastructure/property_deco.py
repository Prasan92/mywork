
class Employee:

    def __init__(self,f_name,s_name):
        self.f_name=f_name
        self.s_name = s_name

    @property
    def email(self):
        return self.f_name + self.s_name +"@gmail.com"

    @property
    def full_name(self):
        return "{} {}".format(self.f_name, self.s_name)

    @full_name.setter
    def full_name(self, name):
        f_name,s_name = name.split(" ")
        self.f_name = f_name
        self.s_name = s_name

emp1=Employee("prasanna", "sekar")
emp2=Employee("kannan", "sekar")p

#emp1.full_name="hrithick roshan"
print(emp1.f_name)
print(emp1.email)
print(emp1.full_name)



