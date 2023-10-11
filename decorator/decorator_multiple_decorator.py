def decorator_fun1(func):
    def wrapper():
        print("decorating with decorator_fun1 ")
        return func()
    return wrapper

def decorator_fun2(func):
    def wrapper():
        print("decorating with decorator_fun2 ")
        return func()
    return wrapper

@decorator_fun1
@decorator_fun2
def some_func():
    print("I am original fn")
    
# syntax
# some_func = decorator_fun1(decorator_fun2(some_func))
some_func()


