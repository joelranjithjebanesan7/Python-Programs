# -*- coding: utf-8 -*-
import random
def get_random_integer(l,min_value,max_value):
    integer_list = []
    for x in range (l) :
        x = random.randint(min_value,max_value) 
        integer_list.append(x)
    return integer_list



l = eval(input("Enter the list length:"))
min_value = eval(input("Enter min value :"))
max_value = eval(input("Enter max value :"))
random_integer_list = get_random_integer(l,min_value,max_value)
print(random_integer_list)