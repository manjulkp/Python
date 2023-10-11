def power(exponent):
    
    def inner(base):
        return base ** exponent
    
    return inner


power_of_two = power(5)
power_of_three = power(5)

# the base value is passed , here we can access exponent - even though power function execution is completed
# the exponent variable , is not variable of inner but of outer fn
# so python will look for it in outer scope - so bascially it will create a closure that as all the reference of variable that part of the inner function
# Non local variable like exponenet is kept in memeory
# since inner has reference to these non local varaible , a closure is created
# a closure - enclosing the non local scoped varaible as part of the inner fn
# a closure - packages inner fn with non local scope variable 

print(power_of_two(base=2))
print(power_of_three(base=3))