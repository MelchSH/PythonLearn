import threading

event = threading.Event()

def function():
    print("Waiting for event")
    event.wait()
    print("Performing action x")

t1 = threading.Thread(target=function)
t1.start()

x = input("Do you want to trigger the event? (y/n): ")
if x == "y":
    event.set()