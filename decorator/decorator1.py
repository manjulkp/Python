
def email_decorator(func):
    def wrapper():
        print("Dear Interns,")
        func()  # different messages can be the template 
        print("Best regards,")
        print("your new boss")
        
    return wrapper

@email_decorator
def greeting_message():
    print("Welcome to your new job")
    
greeting_message()

# greeting_message() has decorator @email_decorator so 
# when it is called it is decorated by @email_decorator fn and returned to the caller
# python interpretor passes original function to the decorator and decorates and returns 
#  so the caller thinks he is actally calling original fn itself

print(greeting_message.__closure__)

print(greeting_message.__closure__[0])
# cell_contents is where the orginal fn is wrapper with all the non local scoped variables
print(greeting_message.__closure__[0].cell_contents)

# the wrapper function memory address 
print(f"0x{id(greeting_message):x}")

    
