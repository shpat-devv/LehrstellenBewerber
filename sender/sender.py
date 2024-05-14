import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate, COMMASPACE
from os.path import basename
import time

from secret import secretgooglekey, googleemail

def send_email(receiver_email, subject, message, attachment_path):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = googleemail
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg['Date'] = formatdate(localtime=True)

        # Attach message body
        msg.attach(MIMEText(message, 'plain'))

        if attachment_path:
            # Open the file to be sent
            with open(attachment_path, "rb") as attachment:
                # Encode the attachment
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={basename(attachment_path)}'
                )
                msg.attach(part)

        # Establish a connection with the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(googleemail, secretgooglekey)
            server.sendmail(googleemail, receiver_email, msg.as_string())

        print("EMAIL HAS BEEN SENT SUCCESSFULLY")

    except Exception as e:
        print(f"Failed to send email: {e}")

