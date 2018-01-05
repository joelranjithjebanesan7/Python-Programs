# -*- coding: utf-8 -*-
def get_kilometer_list(mile_list):
    kilometer_list = []
    for x in mile_list :
        x = format( x*1.6, '.2f')
        kilometer_list.append(x)
    return kilometer_list

mile_list = [12,25,34,27,8]
kilometer_list = get_kilometer_list(mile_list)
print(kilometer_list)        
    