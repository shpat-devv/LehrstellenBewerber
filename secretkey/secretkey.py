from pathlib import Path
import os

googlemail = ""
googlekey = ""
this_path = ""

def save_key_to_file(key, mail):
    global googlekey
    global googlemail
    global this_path
    
    googlekey = key
    googlemail = mail

    try:
        if Path('/_internal').exists():
            with open('_internal/secretkey/googlekey.txt', 'w') as file:
                file.truncate(0)  # Clear the file
                file.write(key)
            this_path = "_internal"
        else:
            with open('secretkey/googlekey.txt', 'w') as file:
                file.truncate(0)  # Clear the file
                file.write(key)
        print("Saved googlekey.txt successfully.")

    except Exception as e:
        print(f"Error saving googlekey.txt: {e}")

    try:
        if Path('/_internal').exists():
            with open('_internal/secretkey/googlemail.txt', 'w') as file:
                file.truncate(0)  # Clear the file
                file.write(mail)
        else:
            with open('secretkey/googlemail.txt', 'w') as file:
                file.truncate(0)  # Clear the file
                file.write(mail)
        print("Saved googlemail.txt successfully.")
    except Exception as e:
        print(f"Error saving googlemail.txt: {e}")

def check_credentials(key_path, mail_path):
    keyavailable = os.path.isfile(key_path) and os.path.getsize(key_path) > 0
    mailavailable = os.path.isfile(mail_path) and os.path.getsize(mail_path) > 0

    if not os.path.isfile(key_path):
        ...
    elif os.path.getsize(key_path) == 0:
        ...
    
    if not os.path.isfile(mail_path):
        ...
    elif os.path.getsize(mail_path) == 0:
        ...

    return keyavailable and mailavailable
