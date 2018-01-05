# -*- coding: utf-8 -*-
pi = 22/7
class Circle(object):
    
    def __init__(self,radius):
        self.radius = radius
    
    def get_area(self):
        return self.radius * self.radius * pi

    def get_circumference(self): 
        return self.radius * pi * 2
