# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import getpass
from email import encoders
from email.mime.text import MIMEText
from session8_1.lab1 import get_page_source
def send_mail(recipent_email,city):
    get_page_source(city)
    user_email = 'joeranjebas@gmail.com'
    password = getpass.unix_getpass()     
    msg = MIMEMultipart()
    msg['Subject'] = 'Wiki Image-' + city
    msg['From'] = user_email
    msg['To'] = recipent_email
    body = "Here i enclosed the wiki image"
    msg.attach(MIMEText(body,'plain'))
    filename = city +".jpeg"
    attachment = open("/home/joelrj/Documents/wiki images/"+ city, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(user_email,password)
    text = msg.as_string()
    server.sendmail(user_email,recipent_email,text)
    server.quit()  
    return 'mailsent'
city = input("enter the city name:")
recipent_email = input("Enter the recipent adress:")
print (send_mail(recipent_email, city))