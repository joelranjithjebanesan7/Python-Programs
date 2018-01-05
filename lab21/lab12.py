# -*- coding: utf-8 -*-
import urllib.request
def get_page_source(name,city):
    url = 'https://en.wikipedia.org/wiki/' + city
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return response.read() 

name = input("Enter your name: ")
city = input("Enter the city name:")
print(get_page_source(name,city))


