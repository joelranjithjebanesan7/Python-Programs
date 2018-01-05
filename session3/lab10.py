# -*- coding: utf-8 -*-
def get_tax(salary):
        
    if(salary <= 250000):
        return "No tax"
    
    elif(salary <= 500000):
        tax = salary*0.05
        return tax
    
    elif(salary <= 1000000):
        tax = salary*0.2
        return tax
    
    elif(salary <= 5000000):
        tax= salary*0.3
        return tax
    
    elif(salary <= 100000000):
        income_tax = salary * 0.3
        surcharge_tax = income_tax * 0.1
        added_tax = income_tax + surcharge_tax
        educational_cess = added_tax*0.02
        high_edu_cess = added_tax*0.01
        tax = added_tax + educational_cess + high_edu_cess
        return tax
    
    else:
        income_tax = salary * 0.3
        surcharge_tax = income_tax * 0.15
        added_tax = income_tax + surcharge_tax
        educational_cess = added_tax * 0.02
        high_edu_cess = added_tax * 0.01
        tax = added_tax + educational_cess + high_edu_cess
        return tax


salary = eval(input("Enter your salary:"))
tax = get_tax(salary)
print("Your tax is:"+str(tax))