
import os
import time
from multiprocessing import Process, current_process


def square(number):
    for num in number:
        time.sleep(0.5)
        result = num * num
        print("the number {} square to {}".format(num, result))


if __name__ == "__main__":
    processes = []
    number = range(20)
    # for i in range(10):
    process = Process(target=square, args=(number,))
    processes.append(process)
    process.start()
    for process in processes:
        process.join()

    print("multiprocessing completed")


"""
import os
from multiprocessing import Process, current_process


def square(number):
    result = number*number

    #process_id = os.getpid()
    #print("the process is {}".format(process_id))
    
    process_name = current_process().name
    print("process name {}".format(process_name))
    print("the number {} square to {}".format(number,result))


if __name__ == "__main__":
    processes = []
    numbers = [1,2,3,4,5]
    for number in numbers:
        process = Process(target = square, args=(number,))
        processes.append(process)
        process.start()
    print(processes)

"""





