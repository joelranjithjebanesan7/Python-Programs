# -*- coding: utf-8 -*-
def get_selling_price(list_price, discount_percentage=10, binding_type="PB"):
    if binding_type == "HB":
        discount = 0
    else:
        discount = list_price * discount_percentage / 100
    
    selling_price = list_price - discount
    return selling_price




print(get_selling_price(150))

print(get_selling_price(150, 20))

print(get_selling_price(150, 30, "PB"))

print(get_selling_price(150, 50, "HB"))

lp = 150
b = "HB"

print(get_selling_price(lp, binding_type=b))
