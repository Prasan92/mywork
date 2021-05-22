import time
import random
import memory_profiler as mem_profile

names=["prasanna","kannan","vasanthi","sekar","roja"]
age=["28","33","32","60","50"]
#print(dir(mem_profile))
print("memory before {}".format(mem_profile.memory_usage()))
def people_list(num):
    result=[]
    for i in range(num):
        people = {
            "id": i,
            "name": random.choice(names),
            "age": random.choice(age)
        }
        result.append(people)
    return result

def people_generator(num):
    for i in range(num):
        people = {
            "id": i,
            "name": random.choice(names),
            "age": random.choice(age)
        }
        yield people

#final = people_list(100000)

final = people_generator(100)
print(final)
next(final)
print("memory after{}".format(mem_profile.memory_usage()))




