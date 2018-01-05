def get_simple_intrest(principal,time,rate):
    
    intrest = (principal*time*rate)/100
    return  intrest

principal = float(input("enter principle amount:"))
time = float(input("no of years:"))
rate = int(input("rate of interest in %:"))
interest = get_simple_intrest(principal, time, rate)
print("Simple Intrest:"+str(interest))