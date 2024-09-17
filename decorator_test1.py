#decorator test

def logged(fun):
    def wrapper(*args,**kwargs):
        value = fun(*args,**kwargs)
        with open("logfile.txt","a+") as f:
            fname = fun.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10,20))