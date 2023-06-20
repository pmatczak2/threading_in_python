import time
import threading



def myfunc(name):
    print(f'myfunc started with {name}')
    time.sleep(10)
    print('myfunc ended')

if __name__ == "__main__":
    print('main started')
    t = threading.Thread(target=myfunc, args=['realpython'])
    t.start()
    t.join()
    print('main ended')

#  The concept of `.join()` is related to thread synchronization and blocking in Python's `threading` module.
#
# When you call the `.join()` method on a thread object, it instructs the calling thread to wait for the completion
# of the target thread before proceeding further. In other words, it blocks the calling thread until the target
# thread has finished executing.
#
# Here's how the concept of `.join()` works:
#
# 1. Starting a Thread: When you create and start a thread using the `.start()` method, it begins its execution in
# parallel with the calling thread.
#
# 2. Blocking with `.join()`: If you want the calling thread to wait until the target thread has finished its
# execution, you can call `.join()` on the thread object. The calling thread will be blocked and won't proceed until
# the target thread completes.
#
# 3. Thread Completion: Once the target thread has finished executing, the calling thread is unblocked, and it can
# continue its execution.
#
# The `.join()` method allows you to ensure that certain parts of your code are executed only after the target thread
# has completed its task. It helps with synchronization and coordination between threads, especially when you need
# the results or side effects of a thread's execution before proceeding with the rest of your program.
#
# Additionally, you can specify a timeout value as an argument to `.join(timeout)`. This sets a maximum time for the
# calling thread to wait for the target thread to complete. If the timeout expires before the target thread finishes,
# the calling thread will resume execution regardless.
#
# In summary, `.join()` is a useful method for controlling the flow and synchronization of threads in Python,
# allowing you to coordinate the execution of multiple threads and ensure that specific tasks are completed before
# proceeding further.