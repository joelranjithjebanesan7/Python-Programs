'''
Created on 16-Nov-2017

@author: joelrj
'''
import sqlite3
import csv
def create_db():
    conn = sqlite3.connect('100_books.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Books")
    c.execute("CREATE TABLE Books(book_id TEXT, title TEXT, author TEXT, binding TEXT, pages INT, price INT, isbn INT, image_url TEXT)")
    with open('/home/joelrj/Documents/100books.csv','r') as csv_file :
        csvReader = csv.DictReader(csv_file)
        value_db = [(i['book_id'], i['title'], i['author'], i['binding'], i['pages'], i['price'], i['isbn'], i['image_url']) for i in csvReader ]
    c.executemany("INSERT INTO Books VALUES(?,?,?,?,?,?,?,?)",value_db)
    conn.commit()
    

create_db()