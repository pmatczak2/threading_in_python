import concurrent.futures
import queue
import random
import threading
import time




class Pipeline(queue.Queue):
# 1. The `Pipeline` class now inherits from `queue.Queue`, which is a built-in thread-safe queue implementation.
# This simplifies the implementation of the pipeline using the queue's methods and features.

    def __init__(self, ):
        super().__init__(maxsize=10)
# 2. The `capacity` parameter was removed from the `Pipeline` constructor since the queue's max size is now set using
# `super().__init__(maxsize=10)`.


    def set_message(self, message):
        print(f'producing message of {message}')
        producer_pipeline.append(message)
        self.put(message)
# 3. The `set_message` method now uses the `put` method of the queue to add a message to the pipeline. It no longer
# checks the queue size explicitly.

    def get_message(self):
        message = self.get()
        print(f"consuming message of {message}")
        consumer_pipeline.append(message)
        return message
# 4. The `get_message` method uses the `get` method of the queue to retrieve a message from the pipeline. It also no
# longer checks the queue size explicitly.


def producer(pipeline, event):
    while not event.is_set():
        message = random.randint(1, 100)
        pipeline.set_message(message)

# 5. The `producer` function now uses a `while` loop with the condition `not event.is_set()` to continuously produce
# messages until the event is set. It generates a random message and adds it to the pipeline using
# `pipeline.set_message(message)`.

def consumer(pipeline, event):
    while not pipeline.empty() or not event.is_set():
        print(f'queue size is {pipeline.qsize()}')
        message = pipeline.get_message()
        time.sleep(random.random())
# 6. The `consumer` function also uses a `while` loop with the condition `not pipeline.empty() or not event.is_set()`
# to continue consuming messages until the pipeline is empty and the event is set. It retrieves messages from the
# pipeline using `pipeline.get_message()`.

producer_pipeline = []
consumer_pipeline = []
if __name__ == "__main__":
    pipeline = Pipeline()
    event = threading.Event()  # .set(), reset()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline, event)
        ex.submit(consumer, pipeline, event)
        time.sleep(0.5)
        event.set()
    print(f"producer: {producer_pipeline}")
    print(f"consumer: {consumer_pipeline}")
# 7. The `event` object of type `threading.Event` is created to coordinate the termination of the producer and consumer
# threads. It is initially unset and is later set using `event.set()` after a short delay of 0.5 seconds to allow some
# messages to be produced.

# Overall, these changes simplify the code by utilizing the thread-safe features of `queue.Queue` and introducing an
# event to control the termination of the threads.