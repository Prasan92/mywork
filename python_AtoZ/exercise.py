class Grand():
    def __init__(self,height):
        self.height = height

class Father(Grand):
    def __init__(self,weight):
        super().__init__(height)
        self.weight = weight

class son(Father):
    def __init__(self,age):
        super().__init__(weight)
        self.age = age

    def body(self):
        print("son age is {} and got his height {} from grand and weight {} from dad".format(self.age,self.height, self.weight))


g = Grand(6)
f = Father(80)

s = son(16)
s.body()