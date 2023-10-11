class Employee:
    def __init__(self):
        self.name = "manjula"
        self.age = 23
        
#  an instance of an object is created 
obj = Employee()
print(obj.__class__)
print(obj.__dict__)