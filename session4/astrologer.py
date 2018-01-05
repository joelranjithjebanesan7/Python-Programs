# -*- coding: utf-8 -*-
import random
past_life = dict()
def get_past_life(user_name):
    past = ("soldier", "president", "police",
            "bird", "flower", "painter", "stone")
    
    if user_name in past_life :
        return past_life[user_name]
    else :
        find_past = past[random.randint(0,(len(past)-1))]
        past_life[user_name] = find_past
        return past_life[user_name]
def get_prediction(user_name):
    predict = ("soldier", "president", "police",
            "bird", "flower", "painter", "stone")
    find_predict = predict[random.randint(0,3)]
    return find_predict

def get_user_value(user_name):
    
    
    option = input("want  your past or prediction p/f?")

    if option == "p":
   
        return(get_past_life(user_name))
    
    elif option  == "f":
    
        return (get_prediction(user_name))

    
    
        
want_again = "yes"
while want_again == "yes" :
    user_name = input("Enter your name:") 
    print(get_user_value(user_name))
    want_again = input("Do you want to continue ? yes/no : ")