from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv
from termcolor import colored

# load env vars
load_dotenv()

os.system("color")

email_sender = os.getenv("MAIL")
print("[{}] Got mail `{}` from env".format(colored("INFO", "yellow"), colored(email_sender, "green")))

email_password = os.getenv("PASSWORD")

# reveiver is a temporary mail
receiver = "vigeyaw971@inkmoto.com"

# Email body
subject = "Don't forget to subscribe"
body = """
        When you watch a video, please hit the subscribe button 
        """

# create email
msg = EmailMessage()

# construct email header
msg["From"] = email_sender
msg["To"] = receiver
msg["Subject"] = subject

# set email body
msg.set_content(body)

# create context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, receiver, msg.as_string())
    print("[{}] Successfully sent email to {}".format(colored("INFO", "yellow"), colored(receiver, "green")))
