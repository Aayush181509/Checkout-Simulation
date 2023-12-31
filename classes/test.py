import concurrent.futures
import threading
import time
import random
# import sys
import os

def worker1():
    while not exit_flag.is_set():
        print("Worker 1 is running",os.getpid())
        time.sleep(random.uniform(1, 3))  # Simulate some work

def worker2():
    while not exit_flag.is_set():
        print("Worker 2 is running",os.getpid())
        time.sleep(random.uniform(2, 4))  # Simulate some work

def monitor_input():
    global exit_flag
    input("Press 'q' to quit: ");
    exit_flag.set()

if __name__ == "__main__":
    exit_flag = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        # Start worker threads
        future1 = pool.submit(worker1)
        # print('Hello')
        future2 = pool.submit(worker2)

        # Start user input monitoring thread
        # input_thread = threading.Thread(target=monitor_input)
        # input_thread.start()

        # # Wait for user input thread to finish
        # input_thread.join()

        # Cancel worker threads
        future1.cancel()
        future2.cancel()

    print("Main thread continuing to run")
