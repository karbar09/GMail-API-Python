from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "from@gmail.com"
toaddr = "to@example.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subject"

body = """
This is the body
"""
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
#username,password
#set USERNAME value to your gmail user name 
#set PASSWORD value to: follow instructions here-- https://support.google.com/accounts/answer/185833

USERNAME = "user"
PASSWORD = "pass"
server.login(USERNAME, PASSWORD)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)