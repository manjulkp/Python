class DecoratorClass:
    
    def __init__(self , some_arg):
        self.some_arg = some_arg
      
    #  call the instance itself  
    def __call__(self, func):
        def wrapper():
            print("Decoartor functionality")
            print(f"{self.some_arg}")
            return func()
        return wrapper
    
def some_func():
        pass
    

obj = DecoratorClass(some_arg="value")
some_func = obj.__call__(some_func)

    
    
# or --> placing class decorator on top of method 
@DecoratorClass(some_arg="value")
def some_func():
    pass
    
        