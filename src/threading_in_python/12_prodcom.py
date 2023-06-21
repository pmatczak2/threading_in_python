import concurrent.futures
import random
import threading
import time

FINISH = "THE END"
# Define a constant variable FINISH set to "THE END". This will be used to indicate the end of message
# production/consumption.

class Pipeline:

    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
    # capacity represents the maximum number of messages the pipeline can hold.
    # message stores the current message produced by the producer.
    # producer_lock is a threading lock used to synchronize access to the message variable during message production.
    # consumer_lock is a threading lock used to synchronize access to the message variable during message consumption.
    # By acquiring this lock initially and not releasing it, we ensure that the consumer waits for the producer to set
    # the message before attempting to consume it.
    def set_message(self, message):
        print(f'producing message of {message}')
        producer_pipeline.append(message)
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()
    # Print a message indicating that a message is being produced.
    # Append the produced message to the producer_pipeline list (a global list defined outside the class).
    # Acquire the producer_lock to ensure exclusive access to the message variable.
    # Set the message variable with the produced message.
    # Release the consumer_lock to signal the consumer that a new message is available for consumption.

    def get_message(self):
        print(f"consuming message of {self.message}")
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        consumer_pipeline.append(message)
        return message
    # Print a message indicating that a message is being consumed.
    # Acquire the consumer_lock to ensure exclusive access to the message variable.
    # Assign the current message to a local variable message.
    # Release the producer_lock to allow the producer to set a new message.
    # Append the consumed message to the consumer_pipeline list (a global list defined outside the class).
    # Return the consumed message.

def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)
# Iterate pipeline.capacity times to produce random messages within the given capacity.
# Call the set_message method of the pipeline object to set each produced message.
# Finally, call set_message with the FINISH constant to indicate the end of message production.

def consumer(pipeline):
    message = None
    while message is not FINISH:
        message = pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())
# It takes a pipeline object as an argument.
# It initializes the message variable to None.
# It enters a loop that continues until the message is equal to FINISH.
# In each iteration, it calls the get_message method of the pipeline object to retrieve a message.
# If the retrieved message is not FINISH, it sleeps for a random duration using time.sleep(random.random()).


producer_pipeline = []
consumer_pipeline = []
if __name__ == "__main__":
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)
    print(f"producer: {producer_pipeline}")
    print(f"consumer: {consumer_pipeline}")
