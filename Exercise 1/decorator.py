# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        multi=function(*args)
        print(f"you called {function.__name__}{args}")
        print(f"It returned: {multi}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def add_fun(a,b,c):
    return a*b*c
args=(1,2,3)
add_fun(*args)
