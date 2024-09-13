import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate, COMMASPACE
from os.path import basename
import os
import time

googleemail = ""
secretgoogle = ""

def set_credentials(mail,key):
    global googleemail
    global secretgooglekey
    googleemail = mail
    secretgooglekey = key

def send_email(receiver_email, subject, message, folder_path):
    global googleemail
    global secretgooglekey
    
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = googleemail
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg['Date'] = formatdate(localtime=True)

        # Attach message body
        msg.attach(MIMEText(message, 'plain'))

        for file in folder_path:
            # Open the file to be sent
            with open(file, "rb") as attachment:
                # Encode the attachment
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={basename(file)}'
                )
                msg.attach(part)

        # Establish a connection with the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(googleemail, secretgooglekey)
            server.sendmail(googleemail, receiver_email, msg.as_string())
        return True

    except Exception as e:
        return False

