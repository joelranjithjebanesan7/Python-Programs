# -*- coding: utf-8 -*-
class UFile(object):
    
    def __init__ (self,name,full_path,size_in_chars=0):
        
        self.name = name
        self.full_path = full_path
        self.size_in_chars = size_in_chars
    
    def write_file(self,content):
        self.content = content
        f=open(self.full_path+self.name,"w")
        f.write(self.content)
        f.close()
    def read_file(self):
        f = open(self.full_path+self.name,"r")
        for line in f.readlines():
            self.size_in_chars = self.size_in_chars + len(line)
        f.close()
        return self.size_in_chars
        


obj = UFile("parts.txt","/home/joelrj/Documents/python/")
content = input('Enter the content:\n')
obj.write_file(content)
print(obj.read_file())