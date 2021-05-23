
def deco(f):
    #check no. of arguments
    def inner(*args):
        try:
            if len(args) != 2:
                raise Exception ("cannot pass more then two arguments")
            a,b=args
            if not (type(a) in [int,float] and type(b) in [int,float]):
                raise Exception ("pass either int or float")
            if b==0:
                raise Exception ("divisible value shouldn't be zero")
            return f(*args)
        except Exception as e:
            return e
    return inner

@deco
def div(a,b):
    return (a/b)

print(div(1,"3"))
