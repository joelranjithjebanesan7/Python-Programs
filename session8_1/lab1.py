# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def get_page_source(city):
    url = 'https://en.wikipedia.org/wiki/' + city
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html= response.read() 
    soup = BeautifulSoup(html,'html.parser')
    for a in soup.find_all("a", attrs={'class':'image'}):
        x = 1
        for img in a.find_all('img'):
            image_url = img['src']
        if x == 1:    
            break     
    image_file ='/home/joelrj/Documents/wiki images/'
    urlretrieve('https:'+image_url,image_file+city) 
    return ('City:{0}'.format(city))

city = input("Enter the city name:")
print(get_page_source(city))



#upload.wikimedia.org/wikipedia/commons/c/ce/Tirunelveli_city.jpg