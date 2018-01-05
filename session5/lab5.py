# -*- coding: utf-8 -*-
import string
class Linguist(object):
    
    def __init__(self,message):
        self.message = message
    def analyse_text(self):
        analyse = dict()
        word_occurance = dict()
        charac_occurance = dict()
        analyse["length of the string"] = len(self.message) 
        self.word_count = 1
        self.charac_count = 0
        for x in self.message :
            if x == " " :
                self.word_count  += 1
            else :
                self.charac_count += 1
        analyse["word count"] = self.word_count
        analyse["no of character"] = self.charac_count
        charac_list = list(self.message)
        word_list = (self.message).split()
        for word in word_list:
            word_occurance[word] = word_list.count(word)
        self.nonrepeat = 0
        for word in word_occurance :
            if word_occurance[word] == 1 :    
                self.nonrepeat  += 1
        analyse["unique word"] = self.nonrepeat
        for letter in charac_list:
            charac_occurance[letter] = charac_list.count(letter)
        self.letter_count = 0
        for letter in charac_occurance :
            if charac_occurance[letter] == 1 :
                self.letter_count += 1
        analyse["unique character"] = self.letter_count
        return analyse
    def is_english(self):
        letter_list = list(self.message)
        result = True
        for letter in letter_list :
            if letter in list(string.ascii_letters) or letter == " " :
                result = True
            else:
                result = False
                break
        return result
            
    
    
obj = Linguist('my name is jamesbond007')
print(obj.is_english())       
        