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