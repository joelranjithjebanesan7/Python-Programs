def get_tax(salary, work_type):
    
    if(work_type=="government"):
        return "No tax"
    else:
        
        tax = int(salary)*0.25
        return tax

salary=input("Enter your income:")
work_type = input("Enter the type(government or non-government):")
tax = get_tax(salary, work_type)
print(tax)