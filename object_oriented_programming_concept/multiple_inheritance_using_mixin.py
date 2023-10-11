class Employee:
    # class variable
    min_wages = 1000
    
    def __init__(self , name , age , position , salary):
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary
        self._annual_salary = None
        
    
    def increase_salary(self , percentage):
        # employee['salary'] =  employee['salary'] * (percentage/100)      
        self._salary =  self._salary * (percentage/100)
        
class SlotsinpectorMixin:
    #  mix has_slots to any class instead of inhertance
    def has_slots(self):
        return hasattr(self, "__slots__")

    #  order is first it looks at SlotsinpectorMixin, then Employee
class Developer(SlotsinpectorMixin, Employee):
    __slot__ = ("framework")
    
    def __init__(self, name , age , position , salary , framework):
        super.__init__(name , age , position , salary)
        self._framework = framework
        
ob = Developer()
# give the method resolution order
print(ob.__mro__)
        
        
    