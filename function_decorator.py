# a decorator is a higher order function which takes another fn and returns a closure

def greeting_message():
    print("Welcome to your new job")
    

def email_decorator(func):
    def wrapper():
        print("Dear Interns,")
        func()  # different messages can be the template 
        print("Best regards,")
        print("your new boss")
        
    return wrapper

# In decorator , it accept a fn and it will wrap that inner function by adding additional behaviour to the wrapper function using closure concept
# here - func() is non local scope varaible here 


#  note we are assigning it a varaible that is same as function name so when the invoker
# calls this greeting_message , it is called with the additional behaviour added
#  the function greeting_message is decorated with additional behaviour
#  the caller thinks he is calling orginal fn , bt he is actually calling a decoratored function 
#  Closure retain variable from a non local scope

#  Closure enclose the inner fn with the extended non local variables to be part of the inner fn
greeting_message = email_decorator(greeting_message)

# this -> greeting_message = email_decorator(greeting_message)
# can be replaced by using as below
@email_decorator
def greeting_message():
    print("Welcome to your new job")


greeting_message()

# Decorator extends functions with additional functionality without modifying the orginal function structure
# the inner function that is decorator is assigned to the identifier that is same as original fnction name 






        
        
    