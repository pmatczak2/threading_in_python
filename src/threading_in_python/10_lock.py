import threading
import concurrent.futures
import time

class Account:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()
    def update(self, transaction, amount):
        print(f'{transaction} thread updating...')
        with self.lock:
            local_copy = self.balance
            local_copy += amount
            time.sleep(1)
            self.balance = local_copy
        print(f'{transaction} thread finishing...')

if __name__ == "__main__":
    account = Account()
    print(f"starting with balance of {account.balance}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in [('Deposit', 50), ('Withdrawal', -150)]:
            ex.submit(account.update, transaction, amount)
    print(f'Ending balance of {account.balance}')


lock = threading.Lock()
print(lock)
lock.acquire()
print(lock)
lock.release()
print(lock)

#
# 1. `lock = threading.Lock()` creates a new `Lock` object and assigns it to the variable `lock`. The `Lock`
# class is provided by the `threading` module in Python's standard library.
#
# 2. `print(lock)` outputs the representation of the `lock` object. This representation typically includes information
# about the lock's state and identity.
#
# 3. `lock.acquire()` is used to acquire the lock. This method attempts to acquire the lock. If the lock is available,
# it is acquired, and the program continues execution. If the lock is already held by another thread, the calling thread
# will block (wait) until the lock becomes available.
# 0
# 4. `print(lock)` outputs the representation of the `lock` object after calling `lock.acquire()`. This will typically
# show information indicating that the lock has been acquired.
#
# 5. `lock.release()` is used to release the lock. This method releases the lock that was previously acquired.
# After releasing the lock, other threads waiting to acquire the lock can proceed.
#
# 6. `print(lock)` outputs the representation of the `lock` object after calling `lock.release()`. This will typically
# show information indicating that the lock has been released and is available for other threads to acquire.
#
# In summary, the code creates a `Lock` object, acquires the lock, releases the lock, and observes the changes in the
# lock's state by printing its representation before and after acquiring and releasing. The `Lock` object provides a
# synchronization mechanism that allows multiple threads to coordinate their access to shared resources and ensure
# data integrity.