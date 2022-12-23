import threading


def thread_function():
    for i in range(1, 100000):
        print(i, " - Thread çalıştı")


def thread_function2():
    for i in range(1, 100000):
        print(i, " -----------------")


thread = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function2)

thread.start()
thread2.start()
