import threading

def function1() -> str:
    for i in range(100):
        print("ONE")

def function2() -> str:
    for i in range(100):
        print("TWO")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
t1.join()
t2.start()