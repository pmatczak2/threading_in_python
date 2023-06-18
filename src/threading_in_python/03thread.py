import time
#  This imports the time module, which provides functions for working with time-related operations.
import threading


#  This imports the threading module, which provides high-level threading interfaces for creating and managing threads
#  in Python.
def myfunc(name):
    print(f'myfunc started with {name}')
    time.sleep(10)
    print('myfunc ended')


# def myfunc(name): This defines a function named myfunc that takes a single parameter name.
# print(f'myfunc started with {name}'): This line prints a message indicating that myfunc has started, along with the
# value of the name parameter.
# time.sleep(10): This line introduces a delay of 10 seconds using the sleep function from the time module. It pauses
# the execution of the current thread (in this case, the main thread or the thread that calls myfunc) for the
# specified number of seconds.
# print('myfunc ended'): This line prints a message indicating that myfunc has ended.

if __name__ == "__main__":
    print('main started')
    t = threading.Thread(target=myfunc, args=['realpython'])
    t.start()
    print('main ended')

# if __name__ == "__main__":: This condition checks if the script is being run as the main module.
# print('main started'): This line prints a message indicating that the main part of the script has started.
# t = threading.Thread(target=myfunc, args=['realpython']): This line creates a new Thread object named t. The target
# parameter specifies the function that will be executed in the new thread, which is myfunc in this case. The args
# parameter provides the arguments to be passed to the myfunc function, which is a list containing the string
# 'realpython'.
# t.start(): This line starts the execution of the thread t by invoking its start() method. This will call the myfunc
# function in a separate thread.
# print('main ended'): This line prints a message indicating that the main part of the script has ended.


# Threading is affecting this code by allowing the myfunc function to be executed concurrently in a separate thread.
# When t.start() is called, a new thread is created and starts executing the myfunc function. Meanwhile, the main thread
# continues executing the remaining code. This means that the line print('main ended') will be executed immediately
# after t.start() without waiting for the myfunc function to complete its execution. As a result, the output of the
# program may appear in a mixed order, with messages from both the main thread and the myfunc thread interleaved.
