#  Class  is real world abstration of attribute and behaviour 


class Employee:
    def __init__(self , name , age , position , salary):
        self.name = name
        
    
    def increase_salary():
        pass
    
    def info():
        pass
    
    
obj = Employee("manjula" , 23 , "qa" , 23000)
print(obj.__class__) # print the class name that generated this obj 




s = str("hello")
num = int(2)

print(s.__class__) # print the class name for string variable

# python is dynamic language
# becos it interprets based on the assignment 
# everything in python is a object 

s1 = "heello"
num1 = 12

