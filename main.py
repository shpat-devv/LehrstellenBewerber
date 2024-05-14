from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *
from sender.sender import send_email
import datetime
import os

# Define the path to the document to be sent
document_name = "Bewerbung/tosend/Bewerbung.pdf"
document_path = os.path.join(os.path.dirname(__file__), document_name)

# Get the current date
current_date = datetime.datetime.now().strftime("%d.%m.%Y")

name = input ("Name: ")
surname = input ("Nachname: ")

while True:
    # Collect input from the user
    apprenticeship = input("Lehre: ")
    salutation = input("Anrede Person (Default = Damen und Herren): ") or "Damen und Herren"
    gender = input("Geschlecht der Person (m oder f): ")
    company_name = input("Firma: ")
    application_address = input("Bewerbungsadresse: ")
    application_location = input("Bewerbungsort: ")
    company_email = input("Firmenmail: ") # email of the company you are applying to
    confirmation = input(f"{company_name}, {application_address}, {application_location}, {company_email}, korrekt? (j/n): ")

    if confirmation.lower() != "j" or not all([apprenticeship, company_name, application_address, application_location, company_email]):
        print("Bitte nochmals eingeben.")
    else:
        print("Changing files...")
        waiting_animation(3)

        # Update the Word document with the provided details
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "DatummutaD", current_date)
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "SDF)Pasdfunpoiva)PHDF(P)S", company_name)
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "()SDFZ=ZHVHHHDUC=P/S78z0f", application_address)
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "c6t89fdsa08967tg", application_location)
        word_to_pdf_converter()

        print("Sending email...")
        waiting_animation(3)

        # Determine the proper salutation based on gender
        if gender == "m":
            salutation = f"Sehr geehrter Herr {salutation}"
        elif gender == "f":
            salutation = f"Sehr geehrte Frau {salutation}"
        else:
            salutation = "Sehr geehrte Damen und Herren"

        # Create the email message
        email_message = f"""
{salutation},

Mein Name ist {name}, und ich interessiere mich sehr für eine Lehrstelle bei Ihrem Unternehmen.

Ich bin äußerst motiviert, bei Ihnen wertvolle Einblicke zu gewinnen und meine Fähigkeiten weiterzuentwickeln. Im Anhang finden Sie meine Bewerbungsunterlagen, bestehend aus meinem Lebenslauf, meiner Bewerbung, meinen Zeugnissen.

Über eine positive Rückmeldung von Ihnen würde ich mich sehr freuen.

Mit freundlichen Grüßen,
{name} {surname}
"""
        # Send the email with the attachment
        send_email(company_email, f"Bewerbung um eine Lehrstelle als {apprenticeship}", email_message, document_path)
        waiting_animation(3)

        # Revert the changes in the Word document
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", company_name, "SDF)Pasdfunpoiva)PHDF(P)S")
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", application_address, "()SDFZ=ZHVHHHDUC=P/S78z0f")
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", application_location, "c6t89fdsa08967tg")
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", current_date, "DatummutaD")
