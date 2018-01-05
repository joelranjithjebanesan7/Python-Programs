# -*- coding:utf-8 -*-
from urllib.request import urlretrieve
import csv
with open('/home/joelrj/Documents/100books.csv') as csvfile :
    
    readCSV = csv.reader (csvfile, delimiter = ',')
    
    urls = []

    for row in readCSV:
        url= row[7]
        urls.append(url)
        
    urls.pop(0)
        
img_counter = 0
for x in urls:
    img_counter+=1
    filename = "image" + str(img_counter) +".jpg"
    path = '/home/joelrj/joel-python/images/'
    urlretrieve(x,path+filename)
print('downloading complete')