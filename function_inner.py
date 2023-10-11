def inner(a,b):
    return a+b

# the local variable a,b are released from the garbage colletor once the function is released from the stack 
# so we cannot access the local variables outside the function


# In python we can use function name to access the function in memory just like string or variable are used to acccess the value in memory
# Inner function inside outer function
# 
def outer():
    # inner function is local scope of outer()
    # so we cannot access outside outer
    
    def inner1():
        print("I am inner function")
        
    inner()
    
outer()

def outer():
    # inner function is local scope of outer()
    # so we cannot access outside outer
    # inorder to access inner function retirn the inner fnction name
    
    #  once the outer fn , completes its execution , we can still access inner fn - how 
    #  becos outer fn has reference to inner fn 
    #  so python - even though outer fn completes its execution , it still has the reference of inner and this is not release from the garabbage collector
    #  so higher order function can be used to return another function [that has all the enclosed local scope variables referenced to this inner fnction so we can access the inner function 
    #  even though the outer fn execution is completed ]
    
    def inner1():
        print("I am inner function")
        
    return inner

func = outer()
func()

print(func)




