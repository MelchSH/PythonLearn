import threading
import time
import os


path = "test.txt"
text = ""
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def readFile():
    global path, text
    while True:
        with open("test.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(10):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t1.start()
t2 = threading.Thread(target=printloop)

t2.start()
t2.join()
