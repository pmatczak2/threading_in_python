import time
import threading



def myfunc1(name):
    print(f'myfunc1 started with {name}')
    time.sleep(10)
    print('myfunc1 ended')

def myfunc2(name):
    print(f'myfunc2 started with {name}')
    time.sleep(10)
    print('myfunc2 ended')

def myfunc3(name):
    print(f'myfunc3 started with {name}')
    time.sleep(10)
    print('myfunc3 ended')



if __name__ == "__main__":
    print('main started')
    t1 = threading.Thread(target=myfunc1, args=['realpython'])
    t1.start()
    t2 = threading.Thread(target=myfunc2, args=['foo'])
    t2.start()
    t3 = threading.Thread(target=myfunc3, args=['bar'])
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('main ended')

# The code you provided demonstrates the concept of multithreading in Python. It involves creating and executing
# multiple threads concurrently to perform independent tasks simultaneously. Let's break down the code and explain
# the concept:
#
# 1. Defining Thread Functions: - Three functions `myfunc1`, `myfunc2`, and `myfunc3` are defined, each taking a
# `name` parameter. These functions represent the tasks that will be executed concurrently in separate threads.
#
# 2. Thread Creation and Execution: - Inside the `if __name__ == "__main__":` block, the main program starts. - Three
# threads, `t1`, `t2`, and `t3`, are created using the `threading.Thread` class. Each thread is associated with one
# of the task functions (`myfunc1`, `myfunc2`, `myfunc3`) and passed the corresponding `name` argument. - The `start(
# )` method is called on each thread to initiate their execution. This launches the threads and allows them to run
# concurrently.
#
# 3. Concurrent Execution: - After starting the threads, they run independently and concurrently with the main
# program. - Each thread executes its respective task function, which includes printing a message, sleeping for 10
# seconds using `time.sleep(10)`, and then printing another message. The purpose of the sleep is to simulate some
# work being done. - Since the tasks are running in separate threads, they can execute concurrently, potentially
# overlapping in time.
#
# 4. Thread Synchronization with `.join()`: - After starting the threads, the main program calls the `.join()` method
# on each thread (`t1.join()`, `t2.join()`, `t3.join()`). - The `.join()` method blocks the main program's execution
# and waits until the respective thread completes its execution. - By calling `.join()` on all threads,
# the main program ensures that it doesn't proceed further until all three threads have finished their tasks. - This
# synchronization with `.join()` guarantees that the main program waits for the completion of all threads before
# continuing.
#
# In summary, this code demonstrates the concept of multithreading by creating multiple threads that execute
# different tasks concurrently. By using `.join()`, the main program can synchronize its execution with the
# completion of the threads, ensuring that all tasks are finished before proceeding further. This allows for parallel
# execution of independent tasks, potentially improving overall performance and efficiency.