import time
import threading



def myfunc(name):
    print(f'myfunc started with {name}')
    time.sleep(10)
    print('myfunc ended')

if __name__ == "__main__":
    print('main started')
    t = threading.Thread(target=myfunc, args=['realpython'], daemon=True)
    t.start()
    print('main ended')


# In Python's `threading` module, the `daemon` parameter is used to specify whether a thread should run as a daemon
# thread or a non-daemon thread. When `daemon=True` is set, it means the thread is a daemon thread.
#
# Here's what it provides:
#
# 1. Daemon Thread: A daemon thread is a background thread that runs without blocking the termination of the main
# program. When the main program finishes, all daemon threads are automatically stopped and terminated, regardless of
# their current state. Daemon threads are useful for background tasks or services that need to run as long as the
# main program is running but don't require explicit termination.
#
# 2. Non-Daemon Thread: A non-daemon thread, on the other hand, is a thread that keeps the program alive until it
# completes its execution. If there are any non-daemon threads still running when the main program finishes,
# the program will wait for those threads to complete before it terminates.
#
# By setting `daemon=True`, you are indicating that the thread should run as a background daemon thread. This is
# useful when you have tasks that don't need to complete before the main program terminates. Daemon threads are
# typically used for tasks that can run indefinitely or tasks that can be safely terminated without affecting the
# integrity of the program.
#
# Note: If you don't explicitly set `daemon=True`, the thread will default to a non-daemon thread, which means the
# program will wait for the thread to complete before it terminates.