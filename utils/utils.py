import sys
import time

message = f"Dear {recipient_name}, My name is Shpat, and I am very interested in an internship at your company. I am highly motivated to gain valuable insights and further develop my skills with you. Attached you will find my application documents, including my resume, certificates, portfolio, and GitHub. I would greatly appreciate a positive response from you. Best regards, Shpat Avdiu"


def waiting_animation(wait_time):
    symbols = ['|', '/', '-', '\\']
    while wait_time > 0:
        for symbol in symbols:
            sys.stdout.write(f'\rloading {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
            wait_time -= 1
    sys.stdout.write('\rDone!     ')
    sys.stdout.flush()


def message_changer(message, recipient_name):
    return message.replace("{recipient_name}", recipient_name)
    
print(message_changer(message, "Shpat"))