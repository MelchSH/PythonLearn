
import time

def timed(fun):
    def wrapper(*args,**kwargs):
        before = time.time()
        fun(*args,**kwargs)
        after = time.time()
        dt = after-before
        funName = fun.__name__
        print(f"{funName} took {dt:.6f} s to run!")
    return wrapper

@timed
def fun(x) -> float:
    result = 1
    for i in range(1,x):
        result *= i
    return result

fun(100000)