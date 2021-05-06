class A:
    a=0
    def __init__(self):
        A.a += 1
        count = A.a
        if count >= 10:
            print(count)
            raise Exception


for i in range(12):
    A()
