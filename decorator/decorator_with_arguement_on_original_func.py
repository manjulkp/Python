def decorator_factory(some_arg):
    def decorator_function(func):
        def wrapper():
            print("function is decorated")
            print(f"function is decorated with arguement :{some_arg}")
            return func()
        return wrapper
    return decorator_function
        

@decorator_factory(some_arg="value")
def some_func():
    print("I am some function")
    
# decorator syntax
some_func =  decorator_factory(some_arg = "value")(some_func)


# decorator_factory - When you create decorators with arguments, the outermost function
# that you define should 
# actually define a decorator function and then return it. 
# That's why I called it a decorator_factory because the function 
# literally defines and returns a new decorator function


# to keep the abstraction same , we need to keep the decorator func same as the orginal function name with _ 
def decorator_function(some_arg):
    def _decorator_function(func):
        def wrapper():
            print("function is decorated")
            print(f"function is decorated with arguement :{some_arg}")
            return func()
        return wrapper
    return _decorator_function
        

@decorator_function(some_arg="value")
def some_func():
    print("I am some function")
    
# decorator syntax
some_func =  decorator_factory(some_arg = "value")(some_func)
# other way syntax
some_func = decorator_function(some_func )