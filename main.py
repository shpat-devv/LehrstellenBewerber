from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *
from sender.sender import send_email, set_credentials
from secretkey.secretkey import *
import datetime
import os
import subprocess
import time

# google credentials
googlemail = ""
googlekey = ""

current_date = datetime.datetime.now().strftime("%d.%m.%Y")

document_name = "Bewerbung/tosend"
document_path = os.path.join(os.path.dirname(__file__), document_name)
files = os.listdir(document_path)
documents = [os.path.join(document_path, file) for file in files if os.path.isfile(os.path.join(document_path, file))]

print("Willkommen zum Bewerbungsautomatisierer von:")
time.sleep(1)
print (ascii_art_name)
time.sleep(1)

ask_for_help = input("Würdest du gerne Hilfe nebenbei haben? (j/n): ")
if ask_for_help.lower() == "j":
    subprocess.Popen(["python", "_internal/help/help.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(3)

if not check_credentials("_internal/secretkey/googlekey.txt", "_internal/secretkey/googlemail.txt"):
    while True:
        googlemail = input("Gib deine Google Mail ein: ")
        googlekey = input("Gib dein Google Key ein: ")

        set_credentials(googlemail, googlekey) # Save the credentials to the email sender
        
        print("Senden einer Testmail...")

        if send_email(googlemail, "Test", "Test", documents):
            save_key_to_file(googlekey, googlemail) # Save the credentials to the secretkeyf
            print("\nEmail wurde an ihnen geschickt, checken sie ihre Email.")
            time.sleep(1)
            break
        else:
            print("Fehler beim Senden der Email! Vielleicht ein Tip fehler?")
else:
    googlekey = open('_internal/secretkey/googlekey.txt').read()
    googlemail = open('_internal/secretkey/googlemail.txt').read()
    set_credentials(googlemail, googlekey)

name = input("\nDein Name: ")
surname = input("Dein Nachname: ")

while True:
    apprenticeship = input("Lehre (Beispiel: Logistiker EFZ): ")
    print("\nhier müssen sie nichts eingeben, einfach Enter drücken falls sie keine Angaben haben.")
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

        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", "DatummutaD", current_date)
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", "SDF)Pasdfunpoiva)PHDF(P)S", company_name)
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", "()SDFZ=ZHVHHHDUC=P/S78z0f", application_address)
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", "c6t89fdsa08967tg", application_location)
        if reason:
            replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD", reason)

        if gender == "m":
            full_salutation = f"geehrter Herr {salutation.split(' ')[1]}"
        elif gender == "f":
            full_salutation = f"geehrte Frau {salutation.split(' ')[1]}"
        else:
            full_salutation = "geehrte Damen und Herren"
        
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", "F(ZUS?DFhv9a8dfs089F/", full_salutation)

        word_to_pdf_converter()

        print("Sending email...")

        send_email(company_email, f"Bewerbung um eine Lehrstelle als {apprenticeship}", get_email_message(full_salutation,name,surname), documents)

        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", company_name, "SDF)Pasdfunpoiva)PHDF(P)S")
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", application_address, "()SDFZ=ZHVHHHDUC=P/S78z0f")
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", application_location, "c6t89fdsa08967tg")
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", current_date, "DatummutaD")
        replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", full_salutation, "F(ZUS?DFhv9a8dfs089F/")
        if reason:
            replace_text_in_docx("_internal/Bewerbung/Bewerbung.docx", reason, "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD")

        print("Email sent successfully!\n")
