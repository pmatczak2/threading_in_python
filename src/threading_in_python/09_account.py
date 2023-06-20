import concurrent.futures
import time

class Account:
    def __init__(self):
        self.balance = 100
    def update(self, transaction, amount):
        print(f'{transaction} thread updating...')
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

# 1. Import the necessary modules `concurrent.futures` and `time`.
# 2. Define a class `Account` with an `__init__` method that initializes the `balance` attribute to 100.
# 3. Define an `update` method within the `Account` class that represents an account balance update.
# It takes two arguments: `transaction` and `amount`.
# 4. Inside the `update` method, print a message indicating that a thread is updating the account balance.
# 5. Create a local copy of the current balance using `local_copy = self.balance`.
# 6. Update the local copy by adding or subtracting the provided `amount`.
# 7. Introduce a 1-second delay using `time.sleep(1)` to simulate some processing time.
# 8. Update the account's actual balance with the value of the local copy: `self.balance = local_copy`.
# 9. Print a message indicating that the thread has finished updating the balance.
# 10. In the `__name__ == "__main__"` block, create an instance of the `Account` class and assign it to the variable
# `account`.
# 11. Print the starting balance of the account.
# 12. Create a `ThreadPoolExecutor` object named `ex` using the `with` statement, specifying a maximum of 2 worker
# threads.
# 13. Enter a loop that iterates over a list of transactions and amounts.
# 14. For each iteration, submit a task to the thread pool using `ex.submit(account.update)`. This schedules the
# `update` method of the `account` object to run concurrently in a separate thread without passing any arguments.
# 15. Once all tasks have been submitted to the thread pool, move on to the next line.
# 16. Finally, print the ending balance of the account, indicating the result of the concurrent updates to the account
# balance.
