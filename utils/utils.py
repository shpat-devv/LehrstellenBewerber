import sys
import time

#message = f"Dear {recipient_name}, My name is Shpat, and I am very interested in an internship at your company. I am highly motivated to gain valuable insights and further develop my skills with you. Attached you will find my application documents, including my resume, certificates, portfolio, and GitHub. I would greatly appreciate a positive response from you. Best regards, Shpat Avdiu"


def waiting_animation(wait_time):
    symbols = ['|', '/', '-', '\\']
    while wait_time > 0:
        for symbol in symbols:
            sys.stdout.write(f'\rloading {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
            wait_time -= 1
    sys.stdout.write('\rDone!     \n')
    sys.stdout.flush()

ascii_art_name = """
  _____    _    _   _____      _    _______ 
 / ____|  | |  | | |  __ \    / \   |__   __|
| (____   | |__| | | |__) |  / _ \     | |   
 \____ \  |  __  | |  ___/  / ___ \    | |   
 _____)|  | |  | | | |     /_/   \_\   | |   
|_____/   |_|  |_| |_|                 |_|   

"""

def get_email_message(full_salutation,name,surname):
    return f"""
{"Sehr "+ full_salutation},

Mein Name ist {name}, und ich interessiere mich sehr für eine Lehrstelle bei Ihrem Unternehmen.

Ich bin äußerst motiviert, bei Ihnen wertvolle Einblicke zu gewinnen und meine Fähigkeiten weiterzuentwickeln. Im Anhang finden Sie meine Bewerbungsunterlagen, bestehend aus meinem Lebenslauf, meiner Bewerbung, meinen Zeugnissen.

Über eine positive Rückmeldung von Ihnen würde ich mich sehr freuen.

Mit freundlichen Grüßen,
{name} {surname}
"""


if __name__ == "__main__":
    print(ascii_art_name)
    print(get_email_message("Herr Mustermann","Max","Mustermann"))