# This is email sender template we are working with is connected to an html template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # This for text
from email.mime.image import MIMEImage  # This for image
# This module care of email transfer protocol
import smtplib
from pathlib import Path
# This allows us to read  and relate with paramater ($name) in the html
from string import Template

# This allows us to read the entire html as a string
template = Template(Path("template.html").read_text())
message = MIMEMultipart()
message["from"] = "Eromonsei Samson"
message["to"] = "test@gmail.com"
message["subject"] = "My First email from python"
# the template is an object of the class Template
body = template.substitute({"name": "Samson"})
message.attach(MIMEText(body, "html"))  # To send text messages
# alternatively
# message.attach(MIMEText(template.substitute({"name":Samson}),"html"))
# message.attach(MIMEText(template.substitute(name="Samson"),"html"))
message.attach(MIMEImage(Path("mask.jpg").read_bytes()))  # To send images

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()      # This is like a greeting to email server
    smtp.starttls()   # this allows allthe command sent to the smtp to be encrypted, turning an insecure connection to a secure conn
    # password used is an app password that is needed to send an email from an app
    smtp.login("test@gmail.com", "eddaxgilrmjoecfb")
    smtp.send_message(message)
    print("Sent....")
