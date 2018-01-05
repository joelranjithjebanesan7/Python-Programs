# -*- coding:utf-8 -*-
class Book(object):
    
    def __init__ (self, book_id, title, 
                  author,binding, pages, 
                  price, isbn, images_url):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.binding = binding
        self.pages = pages
        self.price = price
        self.isbn = isbn
        self.images_url = images_url
    def __str__(self):
        return self.title
        
        