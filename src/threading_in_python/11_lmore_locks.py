import threading
#  This imports the threading module, which provides high-level thread-based concurrency constructs in Python.

rlock = threading.RLock()
#  This creates an instance of the RLock class and assigns it to the variable rlock. RLock stands for reentrant lock,
#  which allows the same thread to acquire the lock multiple times.
rlock.acquire()
#  This line acquires the lock. When a thread calls acquire() on an RLock object, it gains exclusive access to the
#  locked resource. If another thread already holds the lock, the calling thread will block and wait until the lock
#  becomes available.
rlock.release()
# This line releases the lock. When a thread calls release() on an RLock object, it releases the lock it holds,
# allowing other threads to acquire it.
rlock.acquire()
#  This line acquires the lock again. In this case, since RLock is reentrant, the same thread that already holds the
#  lock can acquire it again without blocking itself. This is useful in situations where a function may need to reenter
#  a critical section of code protected by the lock.
print(rlock)
#  This line prints the rlock object. The print() function displays the string representation of the RLock object,
#  which typically includes information about the lock's state.
print(threading.current_thread())
# This line prints information about the current thread. The current_thread() function from the threading module
# returns the Thread object corresponding to the current thread. By calling print() on it, we display information
# about the thread, such as its name and thread ID.

# In summary, the code creates an RLock object, acquires and releases the lock, and then acquires it again. It also
# prints information about the RLock object and the current thread. This demonstrates the reentrant behavior of RLock
# and how a single thread can acquire the lock multiple times.
