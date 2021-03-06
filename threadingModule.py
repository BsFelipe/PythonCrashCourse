# thread = a flow of execution. Like a separate order of instructions.
#          However each thread takes a turn running to achieve concurrency
#          GIL = global interpreter lock,
#          allows only one thread to hold the control of Python interpreter at any one time

# CPU bound = program/task spend most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends  most of it's time waiting for external events (user inputs, web scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(2)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(3)
    print("You drank coffee")


def study():
    time.sleep(4)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee(), args=())
y.start()

z = threading.Thread(target=study(), args=())
z.start()

x.join()
z.join()
y.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
