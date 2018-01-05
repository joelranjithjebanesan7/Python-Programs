# -*- coding: utf-8 -*-
from session5.lab3 import Rectangle
import random
def test():
    x = 0
    while x <= 100 :
        length=random.randint(1,200)
        breadth=random.randint(1,200)
        obj=Rectangle(length,breadth)
        print("Rectangle:"+str(x))
        print("Length:"+str(length))
        print("Breadth:"+str(breadth))
        print("Area of rectangle:"+ str(obj.get_area()))
        print("Perimeter of rectangle:" + str(obj.get_perimeter()))
        x += 1
        
print(test())