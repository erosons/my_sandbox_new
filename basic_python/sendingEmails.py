# This two class takes care of the entire body of the from the sender
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # This for text
from email.mime.image import MIMEImage  # This for image
# This module care of email transfer protocol
import smtplib
from pathlib import Path


message = MIMEMultipart()
message["from"] = "Eromonsei Samson"
message["to"] = "test@gmail.com"
message["subject"] = "My First email from python"
#message.attach(MIMEText("keep up the good work"))
message.attach(MIMEImage(Path("mask.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()      # This is like a greeting to email server
    smtp.starttls()   # this allows allthe command sent to the smtp to be encrypted, turning an insecure connection to a secure conn
    # password used is an app password that is needed to send an email from an app
    smtp.login("test@gmail.com", "zivnlxodpeerthgg")
    smtp.send_message(message)
    print("Sent....")
