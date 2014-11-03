from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from config_remote import FROMADDR,TOADDR,BODY,SUBJECT,USERNAME,PASSWORD

msg = MIMEMultipart()
msg['From'] = FROMADDR
msg['To'] = TOADDR
msg['Subject'] = SUBJECT

body = BODY
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login(USERNAME, PASSWORD)
text = msg.as_string()
server.sendmail(FROMADDR, TOADDR, text)