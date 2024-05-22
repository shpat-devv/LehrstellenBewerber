import os

googlemail = ""
googlekey = ""

def save_key_to_file(key, mail):
    global googlekey
    global googlemail
    
    googlekey = key
    googlemail = mail

    try:
        with open('_internal/secretkey/googlekey.txt', 'w') as file:
            file.truncate(0)  # Clear the file
            file.write(key)
        print("Saved googlekey.txt successfully.")
    except Exception as e:
        print(f"Error saving googlekey.txt: {e}")

    try:
        with open('_internal/secretkey/googlemail.txt', 'w') as file:
            file.truncate(0)  # Clear the file
            file.write(mail)
        print("Saved googlemail.txt successfully.")
    except Exception as e:
        print(f"Error saving googlemail.txt: {e}")

def check_credentials(key_path, mail_path):
    keyavailable = os.path.isfile(key_path) and os.path.getsize(key_path) > 0
    mailavailable = os.path.isfile(mail_path) and os.path.getsize(mail_path) > 0

    if not os.path.isfile(key_path):
        print("File googlekey.txt doesn't exist in secretkey.")
    elif os.path.getsize(key_path) == 0:
        print("File googlekey.txt is empty.")
    
    if not os.path.isfile(mail_path):
        print("File googlemail.txt doesn't exist in secretkey.")
    elif os.path.getsize(mail_path) == 0:
        print("File googlemail.txt is empty.")

    return keyavailable and mailavailable
