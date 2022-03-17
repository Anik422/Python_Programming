from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib
template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Anik Ssha"
message["to"] = "aniks422@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "Anik"}) # {"name": "Anik"} or name="ANik" = same value
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("anik.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sushantashaha026@gmail.com", "sushanto8885")
    smtp.send_message(message)
    print("sent...")