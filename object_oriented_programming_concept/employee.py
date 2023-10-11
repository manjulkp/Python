
class Employee:
    def __init__(self , name , age , position , salary):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary
        self._annual_salary = None
        
    
    def increase_salary(self , percentage):
        # employee['salary'] =  employee['salary'] * (percentage/100)      
        self._salary =  self._salary * (percentage/100)
    
    def info(self):
        print(f"{self._name} is of age {self._age}")
      
    # used to print the instance of object  
    def __str__(self):
        return f"{self._name} is of age {self._age}"
    
    def __rep__(self):
        return f"{repr(self._name)} is of age {repr(self._age)}"
    
    def get_salary(self):
        # return round(self.salary , 2)
        return self._salary
    
        
    @property 
    #  property decorator is add , additional behaviour like setter and getter   
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000 :
            raise ValueError("Min wage is 2000")
        self._salary = salary 
        
    @salary.setter
    # cannot set the attribute
    def salary(self, salary):
        raise AttributeError("Salary is read only")
    
    @property
    #  this is an example for password where we dnot want to give readd
    #  read access to password only set property 
    def age():
        raise AttributeError("Salary is write only")
    
    @age.setter
    def age(self, age):
        if age < 0 :
            raise ValueError("age cannot be 0")
        self._age = age
       
    @property 
    # annual_salary is a computed proprty which is not place 
    # inside __init__ but outside as annual salary is based on salary
    # annual_salary is property that is calculated only when we access it 
    def annual_salary(self):
        return self._salary * 12
    
    
    @property 
    # annual_salary is returned from cache value 
    # only first time it is calculated
    # ortherwise return from cache 
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self._salary * 12
        return  self._annual_salary
        
        

    
    
    
        
        
employee1 = Employee("manjula" , 24 , "QA" , 2300)
employee1.increase_salary(employee1 , )

#  method inside class is called instance method 

# The primary purpose of __repr__ is to provide a string that,
# when passed to the Python interpreter, 
# would recreate the same object.

# In summary, __str__ is used for user-friendly, 
# human-readable representations of objects, while __repr__ is used
# for unambiguous and developer-friendly representations that can 
# recreate the object when evaluated in the Python interpreter.
# Both methods can be defined in a class, 
# and they serve different purposes in Python programming

#?  __class__ which class is reponsible to instaniate the object

#? __ methods are called magic or dunder method

# getter and setter method are used to validate the x before it is set 
