# -*- coding: utf-8 -*-
def get_average_nos(input_values):
    count = 0
    for x in input_values :
        count = count + x
        average = count/4 
    return average


input_values = []
for x in range (4):
    x =eval(input("Enter the numbers:"))
    input_values.append(x) 
average = get_average_nos(input_values)
print(average)