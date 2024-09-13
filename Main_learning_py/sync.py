import threading
import time

x = 8192
lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()

    while x < 16384:
        x *= 2
        print(x)
        time.sleep(0.5)
    print("Reached max. value!")
    lock.release()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(0.5)
    print("Reached min. value")
    lock.release()


t1 = threading.Thread(target=double)
t2 = threading.Thread(target=halve)


t2.start()
t1.start()





