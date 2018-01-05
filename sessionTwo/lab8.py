def selling_price(list_price,binding_type,discount=0.1): 
    
    if(binding_type == "HB"):
        return list_price
    else:
        DiscountPercent= float(list_price) * float(discount)
        DiscountPrice=float(list_price) - float(DiscountPercent)
        return DiscountPrice
    
list_price = input("Enter the list price:")
binding_type = input("Enter binding type:")
discount = input("Enter the discount:")
price = selling_price(list_price, binding_type,discount)
print("Price is:"+ str(price))