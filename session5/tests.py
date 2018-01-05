# -*- coding: utf-8 -*-
from session5.lab1 import Circle
import random
def session_test():
    x = 0
    while x <= 100 :
        radius=random.randint(0,300)
        obj = Circle(radius)
        print("Circle:"+str(x))
        print("For radius:"+str(radius))
        print("Area of Circle:"+str(obj.get_area()))
        print("Circumference of Circle:"+str(obj.get_circumference()))
        x += 1
    

print(session_test())