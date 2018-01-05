# -*- coding: utf-8 -*-
def get_mode(l):
    if len(l) > 1: 
       
        d = {} 
        #empty dic for storing number and its repeated occurance
        for value in l:
            if value not in d:
                d[value] = 1
            else:
                d[value] += 1

        if len(d) == 1:
            return [value]
        else:
            i = 0
            for value in d:
                if i < d[value]:
                    i = d[value]
            modes = []
            for value in d:
                if d[value] == i:
                    mode = (value, i)
                    modes.append(mode)
            return modes
        
    else:
        return l
    
l=eval(input("Enter the list:"))
mode = get_mode(l)
print(mode)