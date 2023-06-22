import concurrent.futures
#  In threading, a semaphore is a synchronization primitive that controls access to a shared resource or a limited
#  number of resources. It allows multiple threads to access the resource concurrently up to a certain limit, called
#  the semaphore's "counter." The counter represents the number of available resource units.
#
# A semaphore has two fundamental operations: `acquire()` and `release()`.
#
# - The `acquire()` operation requests access to the resource. If the semaphore's counter is greater than zero, it
# decrements the counter and allows the thread to proceed, indicating that a resource unit is being used. If the
# counter is zero, the `acquire()` operation blocks the thread until a resource unit becomes available.
#
# - The `release()` operation releases the resource, incrementing the semaphore's counter by one. This allows other
# threads waiting on the semaphore to acquire a resource unit.
#
# Semaphores are often used in scenarios where a limited number of resources are available, such as database
# connections, network connections, or instances of a specific object. By regulating access to these resources using
# semaphores, concurrency control and resource allocation can be effectively managed.
#
# It's important to note that semaphores can be implemented as either binary semaphores or counting semaphores. Binary
# semaphores have a counter limited to 0 or 1, effectively acting as a lock or mutex, allowing only one thread to
# access the resource at a time. Counting semaphores have a counter that can be set to any non-negative integer,
# allowing multiple threads to access the resource up to the counter's value.

import concurrent.futures
import random
import threading
import time

def welcome(semaphore, reached_max_users):
    while True:
        visitor_number = 0
        while not reached_max_users.is_set():
            print(f'welcome visitor #{visitor_number}')
            semaphore.acquire()
            visitor_number += 1
            time.sleep(random.random())
#  The welcome function represents the behavior of welcoming visitors.
# Inside an infinite loop, a visitor_number is initialized to 0.
# While the reached_max_users event is not set (indicating the maximum number of users has not been reached):
# It prints a welcome message for a visitor, incrementing the visitor_number.
# It acquires a lock on the semaphore, effectively reducing the semaphore counter by 1, representing a visitor occupying a resource.
# It introduces some delay using time.sleep to simulate visitor behavior.

def monitor(semaphore, reached_max_users):
    while True:
        print(f'[monitor] semaphore={semaphore._value}')
        time.sleep(3)
        if semaphore._value == 0:
            reached_max_users.set()
            print('[monitor] reached max users!')
            print('[monitor] kicking a user out...')
            semaphore.release()
            time.sleep(0.05)
            reached_max_users.clear()
#The monitor function represents the behavior of monitoring the semaphore and managing the number of users.
# Inside an infinite loop:
# It prints the current value of the semaphore.
# It introduces a delay of 3 seconds using time.sleep.
# If the semaphore value (stored in semaphore._value) is 0 (indicating all resources are occupied by visitors):
# It sets the reached_max_users event, indicating that the maximum number of users has been reached.
# It prints a message indicating the maximum number of users has been reached.
# It releases a lock on the semaphore, effectively increasing the semaphore counter by 1 to allow a user to be "kicked out."
# It introduces a small delay of 0.05 seconds using time.sleep.
# It clears the reached_max_users event to allow the system to welcome new users.


if __name__ == '__main__':
    number_of_users = 50
    reached_max_users = threading.Event()
    semaphore = threading.Semaphore(value=50)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(welcome, semaphore, reached_max_users)
        executor.submit(monitor, semaphore, reached_max_users)
# In the main block:
# A number_of_users variable is defined but not used in the code.
# A reached_max_users event is created to signal when the maximum number of users is reached.
# A semaphore is initialized with a value of 50, indicating that 50 resources (slots for visitors) are available.
# A ThreadPoolExecutor is created with a maximum of 2 worker threads.

# The welcome function and monitor function are submitted to the executor as separate tasks, each with the semaphore
# and reached_max_users as arguments.
# The overall logic of the code is to simulate a system that welcomes visitors up to a maximum number of users
# defined by the semaphore value. The welcome function runs in an infinite loop, welcoming visitors and acquiring
# the semaphore lock, effectively occupying a resource slot. The monitor function continuously checks the semaphore
# value and takes action when the maximum number of users is reached, allowing







# sem = threading.Semaphore(value=50)
# sem.acquire()
# sem.acquire()
# sem.acquire()
# sem.release()
# print(sem._value)
