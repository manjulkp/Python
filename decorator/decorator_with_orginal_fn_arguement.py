from functools import wraps


def email_decorator(func):
    # retain the orginal function meta data we use @wrap decorator
    @wraps(func)
    def wrapper(*args, **kwargs):
        # *args, **kwargs are used to give the ability for the orginal fn to have arguement pass
        # all the positional arg are stored in *args tuple
        # args = ("department_name" , )
        # all "keyword args" are stored in **kwargs
        # kwargs = {}
        print("Dear Interns,")
        func(*args, **kwargs)  # different messages can be the template 
        print("Best regards,")
        print("your new boss")
        
    return wrapper

@email_decorator
def greeting_message(department_name):
    """ Function displays a greeting message """
    print("Welcome to your new - ", department_name)
    print(f"Welcome to your new - {department_name}")
    
greeting_message("CDP")

print(greeting_message.__name__)
#?  __doc__ is meta data that is used to access the docstring 
#  decorator will change the meta data of the orginal fn 
#  meta data like __doc__
#  inorder for the doc string of orginal function be passed to wrapper fn , we can use 
#  import functools 
print(greeting_message.__doc__)

# The whole point of decorators is that they are not intrusive. 
# They should just add some additional functionality to the function 
# while leaving the original function as it is. 
# That is why the decorated function is automatically assigned to the name of the original function 
# because we don't want to or need to know how the decorator works. We just need it to work so that 
# we can continue using the original function with that additional functionality. 
# And this abstraction should also include the awareness of metadata. 
# So whenever you create the decorators, you should use the wraps function to keep the metadata of the 
# original function. As you can see, the usage of the wraps decorator is straightforward and 
# it works without us even knowing how, 