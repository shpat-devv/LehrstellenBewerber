from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *
import datetime

date = datetime.datetime.now()
date = str(date.strftime("%d.%m.%Y"))

Firma = ""
BewerbugnsAdresse = ""
BewerbugnsOrt = ""
FirmenMail = ""

while True:
    Firma = input("Firma: ")
    BewerbugnsAdresse = input("Bewerbungsadresse: ")
    BewerbugnsOrt = input("BewerbungsOrt: ")
    FirmenMail = input("FirmenMail: ") # this is the email of the company you are applying to
    Bestätigung = input(f"{Firma}, {BewerbugnsAdresse}, {BewerbugnsOrt}, {FirmenMail}, korrekt? (j/n): ")
    if not Firma or not BewerbugnsAdresse or not BewerbugnsOrt or not FirmenMail or Bestätigung.lower() != "j":
        print("Bitte nochmals eingeben.")
    else:
        print("changing files..")
        waiting_animation(3)
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "SDF)Pasdfunpoiva)PHDF(P)S", Firma) #change the company file
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "()SDFZ=ZHVHHHDUC=P/S78z0f", BewerbugnsAdresse) #change address file
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "c6t89fdsa08967tg", BewerbugnsOrt) #change address file
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", "DatummutaD", date)
        word_to_pdf_converter() #convert the word file to pdf and move it

        waiting_animation(3)
        #change the files back to the original
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", Firma, "SDF)Pasdfunpoiva)PHDF(P)S") 
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", BewerbugnsAdresse, "()SDFZ=ZHVHHHDUC=P/S78z0f") 
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", BewerbugnsOrt, "c6t89fdsa08967tg") 
        replace_text_in_docx("Bewerbung/Shpat Avdiu.docx", date, "DatummutaD")