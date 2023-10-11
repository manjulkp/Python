def email_decorator(fromWho):
    def _email_decorator(func):
        def wrapper(*args , **kwargs):
            print("Dear Interns,")
            func(*args , **kwargs)  # different messages can be the template 
            print("Best regards,")
            print(f"your {fromWho}")
        return wrapper
    return _email_decorator



@email_decorator(fromWho = "team leader")
def greeting_message(job):
    """ function decoratored when called """
    print(f"Welcome to your new {job}")
    
greeting_message("qa role")