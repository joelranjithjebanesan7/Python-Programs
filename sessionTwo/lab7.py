def find_name_size(name):
    
    a = len(name)
    if (a<4):
        return"Your name is short"
    elif(a>8):
        return "Your name is long"
    else:
        return "well"

name = input("Enter your name:")
result = find_name_size(name)
print(result)
