def decorator_function(func):
    def wrapper():
        print("function is decorated")
        return func()
    return wrapper
        

@decorator_function
def some_func():
    print("I am some function")
    
# Decorator syntax equals to 
some_func = decorator_function(some_func)
    
    