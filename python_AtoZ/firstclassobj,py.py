class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = None

    def add(self):
        self.c = self.a + self.b
        return self.c

obj=A(1,1)
print(obj.add())

class printer:
    def __init__(self,obj):
        self.obj = obj

    def getobj(self):
        return obj.add()

p=printer(obj)

print(p.getobj())