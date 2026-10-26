
def debug(func):
    def warapper(*args,**kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}"for key,value in kwargs.items())
        print(f"calling :{func.__name__} with args {args_values} and kwargs{kwargs_value}")
        return func(*args,**kwargs)


    return warapper

@debug
def hello():
    print("Helloooooo")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("mg",greeting="Hanji==")