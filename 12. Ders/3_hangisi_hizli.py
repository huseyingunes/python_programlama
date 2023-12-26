import time
import concurrent
from concurrent.futures import ThreadPoolExecutor
import threading

start_time = time.time()
sonuclar = []
for i in range(1, 100000):
    sonuclar.append(i * i)
print("--- %s seconds ---" % (time.time() - start_time))



def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    results = []
    for i in range(100000):
        results.append(executor.submit(square, i))

start_time = time.time()
for f in concurrent.futures.as_completed(results):
    pass
print("--- %s seconds ---" % (time.time() - start_time))




sonuclar=[]

def thread_function():
    for i in range(1, 5000000):
        sonuclar.append(i * i)


def thread_function2():
    for i in range(5000000, 10000000):
        sonuclar.append(i * i)

thread = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function2)
start_time = time.time()
thread.start()
thread2.start()
print("--- %s seconds ---" % (time.time() - start_time))