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
        for transaction, amount in [('Deposit', 150), ('Withdrawal', -150)]:
            ex.submit(account.update, transaction, amount)
    print(f'Ending balance of {account.balance}')


#
# - The code begins by importing the necessary modules: `concurrent.futures` and `time`.
# - Next, a `class` named `Account` is defined with an `__init__` method and an `update` method. The `Account`
# class represents a bank account with a starting balance of 100.
# - The `update` method takes two arguments: `transaction` and `amount`. It simulates an update to the account
# balance by printing a message, updating a local copy of the balance, introducing a 1-second delay using
# `time.sleep(1)`, and then updating the account's actual balance.
# - In the `__name__ == "__main__"` block, an instance of the `Account` class is created, and the starting balance
# is printed.
# - A `ThreadPoolExecutor` object named `ex` is created using the `with` statement, specifying a maximum of 2
# worker threads.
# - The code enters a loop that iterates over a list of transactions and amounts. For each iteration, it submits
# a task to the thread pool using `ex.submit(account.update)`. This schedules the `update` method of the `account`
# object to run concurrently in a separate thread, without passing any arguments.
# - Once all the tasks have been submitted to the thread pool, the code moves on to the next line.
# - Finally, the ending balance of the account is printed, indicating the result of the concurrent updates to the
# account balance.
#
# Here's the line-by-line breakdown:
#
# 1. `import concurrent.futures`: Imports the `concurrent.futures` module, which provides a high-level interface for
# asynchronously executing callables in separate threads or processes.
# 2. `import time`: Imports the `time` module, which is used for introducing delays in the code.
# 4. `class Account:`: Begins the definition of the `Account` class.
# 5. `def __init__(self):`: Defines the `__init__` method of the `Account` class. This method initializes the
# `balance` attribute of the `Account` object to 100.
# 7. `def update(self, transaction, amount):`: Defines the `update` method of the `Account` class. This method
# represents an update to the account balance and takes two arguments: `transaction` (a string indicating the type of
# transaction) and `amount` (the amount to be added or subtracted from the balance).
# 9. `print(f'{transaction} thread updating...')`: Prints a message indicating that a transaction is being processed in
# a separate thread.
# 10. `local_copy = self.balance`: Creates a local copy of the current balance.
# 11. `local_copy += amount`: Updates the local copy of the balance by adding or subtracting the given amount.
# 12. `time.sleep(1)`: Introduces a 1-second delay to simulate some processing time.
# 13. `self.balance = local_copy`: Updates