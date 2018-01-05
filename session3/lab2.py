# -*- coding: utf-8 -*-
def get_arithmeic_mean(num_list):
    
    size_of_numbers = len(num_list)
    sum_of_num = 0
    for x in num_list:
        sum_of_num = sum_of_num + x
    mean = sum_of_num / size_of_numbers
    
    return mean

number_list = [1,2,3,4,5]
mean = get_arithmeic_mean(number_list)
print(mean)