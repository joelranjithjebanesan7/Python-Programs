# -*- coding: utf-8 -*-
def get_even_num_list(l):
    even_num_list = []
    for x in range (0,l) :
        even_num_list.append(x*2)
    return even_num_list


l = eval(input("Enter the length of the list:"))
even_number_list = get_even_num_list(l)
print(even_number_list)
        
    