def divisible_or_not(a,b):
    
    if ( a%b == 0):
        return("%s is divisible by %s" %(a,b))
    else:
        return "not divisible"

a=eval(input("enter num1:"))
b=eval(input("enter num2:"))
result = divisible_or_not(a,b)
print(result) 