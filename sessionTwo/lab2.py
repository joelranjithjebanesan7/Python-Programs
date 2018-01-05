def get_cirle_circumference(radius):
    
    circumference = (22 / 7)*2*radius
    return circumference


r = eval(input("Enter the radius:"))
circumference = get_cirle_circumference(r)
print (circumference)