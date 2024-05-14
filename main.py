from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *
from sender.sender import send_email
import datetime
import os

# Get the current date
current_date = datetime.datetime.now().strftime("%d.%m.%Y")

# Define the path to the documents to be sent
document_name = "Bewerbung/tosend"
document_path = os.path.join(os.path.dirname(__file__), document_name)
files = os.listdir(document_path)
documents = [os.path.join(document_path, file) for file in files if os.path.isfile(os.path.join(document_path, file))]

print("Willkommen zum Bewerbungsschreiben Generator von:")
time.sleep(1)
print(ascii_art_name)
time.sleep(1)

name = input("Dein Name: ")
surname = input("Dein Nachname: ")

while True:
    # Collect input from the user
    apprenticeship = input("Lehre: ")
    print("hier müssen sie nichts eingeben, einfach Enter drücken falls sie keine Angaben haben.")
    salutation = input("Anrede Person (Beispiel: Peter Müller): ") or "Damen und Herren"
    print("hier müssen sie nichts eingeben, einfach Enter drücken falls sie keine Angaben haben.")
    gender = input("Geschlecht der Person (m oder f): ")
    company_name = input("Firma: ")
    application_address = input("Bewerbungsadresse: ")
    application_location = input("Bewerbungsort: ")
    company_email = input("Firmenmail: ")  # email of the company you are applying to
    confirmation = input(f"{company_name}, {application_address}, {application_location}, {company_email}, korrekt? (j/n): ")

    if confirmation.lower() != "j" or not all([apprenticeship, company_name, application_address, application_location, company_email]):
        print("Bitte nochmals eingeben.")
    else:
        print("Changing files...")
        waiting_animation(3)

        # Update the Word document with the provided details
        replace_text_in_docx("Bewerbung/Bewerbung.docx", "DatummutaD", current_date)
        replace_text_in_docx("Bewerbung/Bewerbung.docx", "SDF)Pasdfunpoiva)PHDF(P)S", company_name)
        replace_text_in_docx("Bewerbung/Bewerbung.docx", "()SDFZ=ZHVHHHDUC=P/S78z0f", application_address)
        replace_text_in_docx("Bewerbung/Bewerbung.docx", "c6t89fdsa08967tg", application_location)

        # Determine the proper salutation based on gender
        if gender == "m":
            full_salutation = f"geehrter Herr {salutation}"
        elif gender == "f":
            full_salutation = f"geehrte Frau {salutation}"
        else:
            full_salutation = "geehrte Damen und Herren"
        
        replace_text_in_docx("Bewerbung/Bewerbung.docx", "F(ZUS?DFhv9a8dfs089F/", full_salutation)

        word_to_pdf_converter()

        print("Sending email...")
        waiting_animation(3)

        # Create the email message
        email_message = f"""
{"Sehr "+ full_salutation},

Mein Name ist {name}, und ich interessiere mich sehr für eine Lehrstelle bei Ihrem Unternehmen.

Ich bin äußerst motiviert, bei Ihnen wertvolle Einblicke zu gewinnen und meine Fähigkeiten weiterzuentwickeln. Im Anhang finden Sie meine Bewerbungsunterlagen, bestehend aus meinem Lebenslauf, meiner Bewerbung, meinen Zeugnissen.

Über eine positive Rückmeldung von Ihnen würde ich mich sehr freuen.

Mit freundlichen Grüßen,
{name} {surname}
"""
        # Send the email with the attachment
        send_email(company_email, f"Bewerbung um eine Lehrstelle als {apprenticeship}", email_message, documents)

        # Revert the changes in the Word document
        replace_text_in_docx("Bewerbung/Bewerbung.docx", company_name, "SDF)Pasdfunpoiva)PHDF(P)S")
        replace_text_in_docx("Bewerbung/Bewerbung.docx", application_address, "()SDFZ=ZHVHHHDUC=P/S78z0f")
        replace_text_in_docx("Bewerbung/Bewerbung.docx", application_location, "c6t89fdsa08967tg")
        replace_text_in_docx("Bewerbung/Bewerbung.docx", current_date, "DatummutaD")
        replace_text_in_docx("Bewerbung/Bewerbung.docx", full_salutation, "F(ZUS?DFhv9a8dfs089F/")
