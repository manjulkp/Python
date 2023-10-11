def remainder_division1(a,b):
    if b == 0:
        raise ZeroDivisionError
    result = a//b
    remainder = a%b
    print ( a , '/' , b , 'is' , result , 'remainder' , remainder )
    
def remainder_division2(a,b):
    if b == 0:
        raise Exception('In Division , the denominator cannot be zero')
    result = a//b
    remainder = a%b
    print ( a , '/' , b , 'is' , result , 'remainder' , remainder )
    

remainder_division1(10,2)

remainder_division2(10,0)
    
    