from sender.sender import send_email, set_credentials
from secretkey.secretkey import *
from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *
from pathlib import Path
import datetime
import os
import subprocess
import time

# google gmail credentials
googlemail = ""
googlekey = ""

# Define this_path to point to the directory of the script
this_path = os.path.dirname(os.path.realpath(__file__))

current_date = datetime.datetime.now().strftime("%d.%m.%Y")

document_name = "Bewerbung/tosend"
document_path = os.path.join(this_path, document_name)  # Use this_path here
files = os.listdir(document_path)
documents = [os.path.join(document_path, file) for file in files if os.path.isfile(os.path.join(document_path, file))]

print("Willkommen zum Bewerbungsautomatisierer von:")
time.sleep(1)
print(ascii_art_name)
time.sleep(1)

ask_for_help = input("Würdest du gerne Hilfe nebenbei haben? (j/n): ")
if ask_for_help.lower() == "j":
    try:
        subprocess.Popen(["python", os.path.join(this_path, "help", "help.py")], creationflags=subprocess.CREATE_NEW_CONSOLE)
        time.sleep(3)
    except AttributeError:
        print("Tut mir Leid da ist etwas schief gelaufen...")
        waiting_animation(5)

if not check_credentials(os.path.join(this_path, "secretkey", "googlekey.txt"), os.path.join(this_path, "secretkey", "googlemail.txt")):
    while True:
        googlemail = input("Gib deine Google Mail ein: ")
        googlekey = input("Gib dein Google Key ein: ")

        set_credentials(googlemail, googlekey)  # Save the credentials to the email sender

        print("Senden einer Testmail...")

        if send_email(googlemail, "Test", "Test", documents):
            save_key_to_file(googlekey, googlemail)
            print("\nEmail wurde an Ihnen geschickt, checken Sie Ihre Email.")
            time.sleep(1)
            break
        else:
            print("Fehler beim Senden der Email! Vielleicht ein Tippfehler?")
else:
    try:
        googlekey = open(os.path.join(this_path, "secretkey", "googlekey.txt")).read()
        googlemail = open(os.path.join(this_path, "secretkey", "googlemail.txt")).read()
    except:
        print("Error loading keys")

    set_credentials(googlemail, googlekey)

name = input("\nDein Name: ")
surname = input("Dein Nachname: ")

while True:
    apprenticeship = input("Lehre (Beispiel: Logistiker EFZ): ")
    print("\nHier müssen Sie nichts eingeben, einfach Enter drücken, falls Sie keine Angaben haben.")
    time.sleep(1)
    salutation = input("\nAnrede Person (Beispiel: Peter Müller): ") or "Damen und Herren"
    gender = input("Geschlecht der Person (m oder f): ")
    company_name = input("\nFirma: ")
    application_address = input("Bewerbungsadresse: ")
    application_location = input("Bewerbungsort: ")
    company_email = input("Firmenmail: ")
    reason = input("\nWieso willst du die Lehre bei dieser Firma machen? (optional): ")
    confirmation = input(f"\nFirma Name:\t{company_name}\nAdresse:\t{application_address}\nOrt:\t\t{application_location}\nEmail:\t\t{company_email}\n\nAlles korrekt? (j/n): ")

    if confirmation.lower() != "j" or not all([apprenticeship, company_name, application_address, application_location, company_email]):
        continue
    else:
        print("Changing files...")
        waiting_animation(3)

        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), "DatummutaD", current_date)
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), "SDF)Pasdfunpoiva)PHDF(P)S", company_name)
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), "()SDFZ=ZHVHHHDUC=P/S78z0f", application_address)
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), "c6t89fdsa08967tg", application_location)
        if reason:
            replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD", reason)

        if gender == "m":
            full_salutation = f"geehrter Herr {salutation.split(' ')[1]}"
        elif gender == "f":
            full_salutation = f"geehrte Frau {salutation.split(' ')[1]}"
        else:
            full_salutation = "geehrte Damen und Herren"
        
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), "F(ZUS?DFhv9a8dfs089F/", full_salutation)

        word_to_pdf_converter()

        print("Sending email...")

        send_email(company_email, f"Bewerbung um eine Lehrstelle als {apprenticeship}", get_email_message(full_salutation, name, surname), documents)

        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), company_name, "SDF)Pasdfunpoiva)PHDF(P)S")
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), application_address, "()SDFZ=ZHVHHHDUC=P/S78z0f")
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), application_location, "c6t89fdsa08967tg")
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), current_date, "DatummutaD")
        replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), full_salutation, "F(ZUS?DFhv9a8dfs089F/")
        if reason:
            replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), reason, "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD")

        print("Email sent successfully!\n")
