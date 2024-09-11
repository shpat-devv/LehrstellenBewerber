from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *
from sender.sender import send_email
import datetime
import os
import subprocess
# Get the current date
current_date = datetime.datetime.now().strftime("%d.%m.%Y")

# Define the path to the documents to be sent

print(os.path.dirname(__file__))

application_path = os.path.join(os.path.dirname(__file__), "Bewerbung/Bewerbung.docx")
document_name = "Bewerbung/tosend"
document_path = os.path.join(os.path.dirname(__file__), document_name)
files = os.listdir(document_path)
documents = [os.path.join(document_path, file) for file in files if os.path.isfile(os.path.join(document_path, file))]

print("Willkommen zum Bewerbungsschreiben Generator von:")
time.sleep(1)
print(ascii_art_name)
time.sleep(1)
ask_for_help = input("Würdest du gerne Hilfe nebenbei haben? (j/n): ")

if ask_for_help.lower() == "j":
    subprocess.Popen(["python", "help/help.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(3)

name = input("Dein Name: ")
surname = input("Dein Nachname: ")

while True:
    # Collect input from the user
    apprenticeship = input("Lehre: ")
    print("hier müssen sie nichts eingeben, einfach Enter drücken falls sie keine Angaben haben.")
    time.sleep(1)
    salutation = input("Anrede Person (Beispiel: Peter Müller): ") or "Damen und Herren"
    gender = input("Geschlecht der Person (m oder f): ")
    company_name = input("Firma: ")
    application_address = input("Bewerbungsadresse: ")
    application_location = input("Bewerbungsort: ")
    company_email = input("Firmenmail: ")  # email of the company you are applying to
    reason = input("Wieso willst du die Lehre bei dieser Firma machen? (optional): ")
    confirmation = input(f"{company_name}, {application_address}, {application_location}, {company_email}, korrekt? (j/n): ")

    if confirmation.lower() != "j" or not all([apprenticeship, company_name, application_address, application_location, company_email]):
        print("Bitte nochmals eingeben.")
    else:
        print("Changing files...")
        waiting_animation(3)

        first_name = salutation.split(" ")[0]
        last_name = salutation.split(" ")[1]

        # Update the Word document with the provided details
        replace_text_in_docx(application_path, "DatummutaD", current_date)
        replace_text_in_docx(application_path, "SDF)Pasdfunpoiva)PHDF(P)S", company_name)
        replace_text_in_docx(application_path, "()SDFZ=ZHVHHHDUC=P/S78z0f", application_address)
        replace_text_in_docx(application_path, "c6t89fdsa08967tg", application_location)
        if reason:
            replace_text_in_docx(application_path, "sdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASDsdf’78a’dfuihspdoifhpa98P(CZUP)(SDIFHPKSJDczhd098g’asdfu8››9872371›48/&»ç+ç&z07czdh7p9uhcsDFHAPSDUFHASD", reason)

        # Determine the proper salutation based on gender
        if gender == "m":
            full_salutation = f"geehrter Herr {last_name}"
        elif gender == "f":
            full_salutation = f"geehrte Frau {last_name}"
        else:
            full_salutation = "geehrte Damen und Herren"
        
        replace_text_in_docx(application_path, "F(ZUS?DFhv9a8dfs089F/", last_name)

        word_to_pdf_converter(application_path, document_path)

        print("Sending email...")
        waiting_animation(3)

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


