from gmailadapter import GMILAdapter
from message import Welcome
from AdressBook import EmailAndName, RandomImeg
import smtplib

welcom = Welcome()

emailandname = EmailAndName()
email = emailandname[0]
name = emailandname[1]
imege = RandomImeg()
mail = GMILAdapter(
    host="smtp.gmail.com",
    port=465,
    username='twojemail@gmail.com',
    passworrd='password')
mail.login()
mail.send_mail(f"{email}", "Ważna informacja!!", welcom.render(name=f'{name}', imege=imege))
