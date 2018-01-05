# -*- coding: utf-8 -*-
import csv

with open('/home/joelrj/Documents/100books.csv') as csvfile :
    
    readCSV = csv.reader (csvfile, delimiter = ',')
    
    titles = []

    for row in readCSV:
        
        title = row [1]
        
        titles.append(title)
    
    print(titles)
