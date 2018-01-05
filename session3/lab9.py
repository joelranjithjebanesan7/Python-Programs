# -*- coding: utf-8 -*-
def get_fahrenheit_list(celcius_list):
    fahrenheit_list = []
    for x in celcius_list :
        x = x-32
        x = format(x*5/9, '.2f')
        fahrenheit_list.append(x)
    return fahrenheit_list

celcius_list = [92,125,234,127,85]
fahrenheit_list = get_fahrenheit_list(celcius_list)
print(fahrenheit_list)        
    