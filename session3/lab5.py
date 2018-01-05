# -*- coding: utf-8 -*-
import random
def get_random_integer(l):
    integer_list = []
    for x in range (l) :
        x = random.randint(0,100) 
        integer_list.append(x)
    return integer_list


l = eval(input("Enter the list length:"))
random_integer_list = get_random_integer(l)
print(random_integer_list)