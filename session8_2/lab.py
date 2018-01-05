import re
def validate_indian_mobile():
    
    #rule = re.match(r'[789]\d{9}$',value) 
    #rule = re.compile(r'^\+(91)?(0|7){10}$')
    #if re.match(r'^\+[789]\d{9}$',value): 
    if re.match(r'^([+][9][1]|[9][1]|[0]){0,1}([7-9]{1})([0-9]{9})$',phone_num):   
        msg = "This is an indian mobile number."
        return  msg
 
    else:
        msg = "Sorry! Not an indian number"
        return msg

def validate_indian_pin():
    
    if re.match(r'^[0-9]{6}$',pin_code):
        msg = "Indian pincode"
        return msg
    else:
        msg = "Not an Indian pincode!"
        return msg
    
    

phone_num = input("enter the number:")
print (validate_indian_mobile())
pin_code = input("Enter the pincode:")
print(validate_indian_pin())