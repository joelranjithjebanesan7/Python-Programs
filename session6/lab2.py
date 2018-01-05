#-*- coding: utf-8 -*-
class Letter(object):
 
    def __init__ (self, subject, sender_name,
                  sender_address, recipent_name,
                  recipent_gender, body, signature):
        
        self.subject = subject
        self.sender_name = sender_name
        self.sender_address = sender_address
        self.recipent_name = recipent_name
        self.recipent_gender = recipent_gender
        self.body = body
        self.signature = signature 
        
    def compose(self):
        
        self.letter_from = ("From,\n    " + self.sender_name + "\n    "
                       +self.sender_address + "\n")
        
        self.letter_to = ("To,\n    " + self.recipent_name + "\n\n" + 
                          self.recipent_gender + "," + "\n\t")
        self.letter_body = ( self.body + "\n\n\t\t\t\tThanking You," 
                             + "\n\t\t\t\t\t\t\t  Yours truly,")
        self.letter_sign = ("\n\t\t\t\t\t\t\t    " + self.signature )

        return (self.letter_from + self.letter_to 
               + self.letter_body + self.letter_sign )
        
        
obj = Letter ("letter","Joel","Tuticorin","The H.R","Sir/Mam",
              "As I am suffering from fever I am unable to attend the program.","A.JoelRJ.")
print(obj.compose())