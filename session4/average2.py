# -*- coding: utf-8 -*-
def get_average_nos(input_list):

    count = 0
    for x in input_list :
        count = count + x
    average = count/len(input_list) 
    return average


input_list = []
list_len = eval(input('How many numbers to find the average:'))
while(list_len >0):
    num = eval(input("Enter the numbers:  "))
    input_list.append(num) 
    list_len = list_len-1
average1 = get_average_nos(input_list)
print(average1)
    