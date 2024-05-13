import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
from secret import secretgooglekey, googleemail

attachment_path = "Bewerbung.docx"

def send_email(receiver_email, subject, message):
    global attachment_path

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = googleemail
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach message body
    msg.attach(MIMEText(message, 'plain'))

    if attachment_path:
        # Open the file to be sent
        with open(attachment_path, "rb") as attachment:
            # Set attachment filename and content type
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path}",
        )

        # Add attachment to message and convert message to string
        msg.attach(part)

    # Establish a connection with the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(googleemail, secretgooglekey)
        server.sendmail(googleemail, receiver_email, msg.as_string())

    print("EMAIL HAS BEEN SENT SUCCESSFULLY")
