import datetime
import os
import subprocess
import time

from sender.sender import send_email, set_credentials
from secretkey.secretkey import *
from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *

# google gmail credentials
googlemail = ""
googlekey = ""

# Define this_path to point to the directory of the script
this_path = os.path.dirname(os.path.realpath(__file__))

current_date = datetime.datetime.now().strftime("%d.%m.%Y")

application_path = os.path.join(os.path.dirname(__file__), "Bewerbung/Bewerbung.docx")
files_to_send = os.path.join(this_path, "Bewerbung/tosend")  
files = os.listdir(files_to_send)
documents = [os.path.join(files_to_send, file) for file in files if os.path.isfile(os.path.join(files_to_send, file))]

print("Willkommen zum Bewerbungsautomatisierer von:")
time.sleep(1)
print(ascii_art_name)
time.sleep(1)

ask_for_help = input("Würdest du gerne Hilfe nebenbei haben? (j/n): ")
if ask_for_help.lower() == "j":
    try:
        subprocess.Popen(["python", "help/help.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        time.sleep(3)
    except AttributeError:
        print("Tut mir Leid da ist etwas schief gelaufen...")
        waiting_animation(5)

else:
    print("checken nach google Anmeldeinformationen...")
    waiting_animation(3)

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

            first_name = salutation.split(" ")[0]
            last_name = salutation.split(" ")[1]

            # Update the Word document with the provided details
            replace_text_in_docx(application_path, "SDF)Pasdfunpoiva)PHDF(P)S", company_name)
            replace_text_in_docx(application_path, "()SDFZ=ZHVHHHDUC=P/S78z0f", application_address)
            replace_text_in_docx(application_path, "c6t89fdsa08967tg", application_location)
            replace_text_in_docx(application_path, "DatummutaD", current_date)

            if reason:
                replace_text_in_docx(application_path, "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD", reason)
            if gender == "m":
                full_salutation = f"Sehr geehrter Herr {last_name}"
            elif gender == "f":
                full_salutation = f"Sehr geehrte Frau {last_name}"
            else:
                full_salutation = "Sehr geehrte Damen und Herren"
            
            replace_text_in_docx(application_path, "F(ZUS?DFhv9a8dfs089F/", full_salutation)

            word_to_pdf_converter(application_path, this_path)

            print("Sending email...")

            # Create the email message
            email_message = f"""
                {"Sehr "+ full_salutation},

                Mein Name ist {name}, und ich interessiere mich sehr für eine Lehrstelle als {apprenticeship} bei Ihrem Unternehmen.

                Mit großem Interesse verfolge ich die Entwicklungen in Ihrem Unternehmen und sehe in Ihnen einen hervorragenden Ausbildungsbetrieb, der mir die Möglichkeit bietet, wertvolle berufliche Erfahrungen zu sammeln und meine Fähigkeiten weiterzuentwickeln. Die Logistikbranche fasziniert mich besonders, da sie vielseitig und entscheidend für reibungslose Abläufe in nahezu allen Wirtschaftssektoren ist.

                Im Anhang finden Sie meine vollständigen Bewerbungsunterlagen, bestehend aus meinem Lebenslauf, meinem Bewerbungsschreiben sowie meinen Zeugnissen. Ich bin hoch motiviert und freue mich sehr darauf, die Chance zu erhalten, mich persönlich bei Ihnen vorzustellen und Sie von meiner Eignung zu überzeugen.

                Über eine positive Rückmeldung von Ihnen würde ich mich sehr freuen.

                Mit freundlichen Grüßen,
                {name} {surname}
            """
            # Send the email with the attachment
            send_email(company_email, f"Bewerbung um eine Lehrstelle als {apprenticeship}", email_message, documents)

            # Revert the changes in the Word document
            replace_text_in_docx(application_path, company_name, "SDF)Pasdfunpoiva)PHDF(P)S")
            replace_text_in_docx(application_path, application_address, "()SDFZ=ZHVHHHDUC=P/S78z0f")
            replace_text_in_docx(application_path, application_location, "c6t89fdsa08967tg")
            replace_text_in_docx(application_path, current_date, "DatummutaD")
            replace_text_in_docx(application_path, full_salutation, "F(ZUS?DFhv9a8dfs089F/")

            if reason:
                replace_text_in_docx(application_path, reason, "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD")


                replace_text_in_docx(os.path.join(this_path, "Bewerbung", "Bewerbung.docx"), reason, "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD")

            print("Email sent successfully!\n")
