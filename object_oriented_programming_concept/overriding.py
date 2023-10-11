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
        
class Tester(Employee):
    def run_tests(self):
        print("run tests")
        
class Developer(Employee):
    # add attribute to child class 
    def __init__(self, name , age , position , salary , framework):
        super.__init__(name , age , position , salary)
        self._framework = framework
        
    #  method is overriding , parent method is rewritten in child class
    def increase_salary(self , percentage , bonus = 0):
        self._salary =  self._salary * (percentage/100)
        self._salary = self._salary + bonus
        
    def increase_salary_better_way(self , percentage , bonus = 0):
        super().increase_salary(percentage)
        self._salary = self._salary + bonus
        
class Employee1:
    #  to reduce the memory allocated to attribute se __slot__ method
    # provide faster access , by saving the space for attribute
    #  cons is we cannot add attribute dynamic to the instance of the object 
    __slots__ = ("name" , "age" , "position" , "salary")
    
    def __init__(self , name , age , position , salary):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary
        self._annual_salary = None
        

    
        
        
        
emp = Tester
print(isinstance(emp , Tester))
#  return true
print(issubclass(Tester , Employee))
print(issubclass(Employee , object ))


        

        
        