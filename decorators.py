"""def decorator(function) -> None:

    def wrapper():
        print("decorating function")
        function()

    return wrapper

def helloworld():
    print("hello world")

decorator(helloworld)()"""

def decorator(fun) -> None:
    def wrapper(*args,**kwargs):
        return_val = fun(*args,**kwargs)
        print("decor. action")
        return return_val
    return wrapper

@decorator
def helloworld(name) -> str:
    print("first output")
    return f"Hello {name}!"

print(helloworld("MASH"))



