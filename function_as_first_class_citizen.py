def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

# plus is the new reference to function object add 
#  we can use plus instead of add
#  both are pointing to same object 
plus = add 


print(plus(2,3))
print(add)
print(plus)

#  fnction are stored as function object 
#  since function are first class object , the function identifier/name can be used assign to another variable
#  like plus = add 
#  

operation = [add , subtract]

value = operation[0](1,2)
print(value)

# so function object can be assigned to variables and we can play around just like class object 
# 


# function that take another function or retrn another function are called higher order function

def calculator(operation , a,b):
    return operation(a,b)

print(calculator(add(2,3)))
print(calculator(subtract(2,3)))