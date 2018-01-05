# -*- coding: utf-8 -*-
import shutil
import os
class Backup_Agent(object):
 
    def backup_filename(self): 
        self.source= "/home/joelrj/joel-python/session6"
        self.backup = "/home/joelrj/Documents/Backups2"
        shutil.copytree(self.source,self.backup)
        return (os.listdir(self.backup))
    

obj = Backup_Agent()
obj.backup_filename()