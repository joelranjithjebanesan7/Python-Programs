# -*- coding: utf-8 -*-
import random

class Astrologer(object):
    past_life =  dict ()
    predict_life = dict ()
    
    def __init__(self,user_name):
        self.user_name = user_name
        self.lives = ("President", "Police", "Architect", 
                      "Politician", "Teacher", "Bird", "Animal",
                      "Stone")
    
    def get_past_life(self):
        if self.user_name in self.past_life :
            return self.past_life[self.user_name]
        else :
            self.past_life[self.user_name] =  self.lives[random.randint(0,(len(self.lives)-1))]
            return self.past_life[self.user_name]
    def get_predict_life(self):
        if self.user_name in self.predict_life :
            return self.predict_life[self.user_name]
        else :
            self.predict_life[self.user_name] =  self.lives[random.randint(0,(len(self.lives)-1))]
            return self.predict_life[self.user_name]




def get_user_value():
    user_name = input("Enter your name:")
    option = input("Do You want your past or predicion p/f ?")
    obj = Astrologer(user_name)    
    if option == "p":
        print(obj.get_past_life())
    elif option  == "f":
        print(obj.get_predict_life())
    else :
        print("sorry you have enter a wrong value")

want_again = 'yes'

while want_again == "yes" :
    get_user_value()
    want_again = input("do you want to continue ? yes/no")

        
            
            
        
        
    
    