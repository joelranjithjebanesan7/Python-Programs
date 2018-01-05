# -*- coding: utf-8 -*-
def get_median(l):
    l.sort()
    total_num=len(l)
    if total_num%2 != 0 :
        total_num = int(total_num/2)
        median=l[total_num]
        return median
    
    else:
        mid_num1 = int((total_num/2))
        mid_num2= mid_num1-1
        num_sum= l[mid_num1]+l[mid_num2]
        median = num_sum/2
        return median

#a = [9,8,7,6,5,4,3,2,1,0,10]
a = eval(input("Enter the list:"))
median = get_median(a)
print(median)