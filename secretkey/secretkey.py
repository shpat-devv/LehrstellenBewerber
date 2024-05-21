import os

googlemail = ""
googlekey = ""

def save_key_to_file(key, mail):
    global googlekey
    global googlemail
    
    googlekey = key
    googlemail = mail

    with open('secretkey/googlekey.txt', 'w') as file:
        file.truncate(0)  # Clear the file
        file.write(key)

    with open('secretkey/googlemail.txt', 'w') as file:
        file.truncate(0)  # Clear the file
        file.write(mail)


import os

def check_credentials(key_path, mail_path):
    keyavailable = os.path.isfile(key_path) and os.path.getsize(key_path) > 0
    mailavailable = os.path.isfile(mail_path) and os.path.getsize(mail_path) > 0

    # Debug prints to understand the state
    if not os.path.isfile(key_path):
        print("File googlekey.txt doesnt exist in secretkey.")
    elif os.path.getsize(key_path) == 0:
        ...
    
    if not os.path.isfile(mail_path):
        print("File googlemail.txt doesnt exist in secretkey.")
    elif os.path.getsize(mail_path) == 0:
        ...

    return keyavailable and mailavailable
