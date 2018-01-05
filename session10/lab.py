import imaplib
import getpass

class ImapInbox(object):
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    
    def get_mail(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self.username,self.password)
        mail.list()
        msg = mail.select('inbox')
        return msg
    

username = input("enter your mail:")
password = getpass.unix_getpass(prompt = 'Password')
obj = ImapInbox(username,password)
print(obj.get_mail())
    