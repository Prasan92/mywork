from threading import Thread
from time import time, sleep
import requests

out = []
def func():
    res = requests.get("https://jsonplaceholder.typicode.com/users").json()
    out.append(res)

def main():
    t1 = time()
    for i in range(10):
        func()
    t2 = time()
    print("time took {}".format(t2-t1))
    print(out)

def mainthread():
    threads = []
    t1 = time()
    for i in range(10):
        t = Thread(target = func)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    t2 = time()
    print("time took {}".format(t2 - t1))
    print(out)

if __name__ == "__main__":
    #mainthread()
    main()


"""
from threading import Thread
from time import sleep, time

start = time()

def do_something(seconds):
    print("sleeping {} seconds".format(seconds))
    sleep(seconds)
    print("done sleeping")

threads=[]
for _ in range(10):
    t=Thread(target = do_something, args=[1.5])
    t.start()
    threads.append(t)

for i in threads:
    i.join()

# t1=Thread(target = do_something)
# t2=Thread(target = do_something)


finish = time()

print("time took {}".format(finish-start))

"""