import concurrent
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    results = []
    for i in range(10):
        results.append(executor.submit(square, i))


for f in concurrent.futures.as_completed(results):
    print(f.result())
