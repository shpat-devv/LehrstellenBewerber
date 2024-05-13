from utils.utils import *
from changer.wordchanger import *
from changer.wordtopdf import *

Firma = ""
BewerbugnsAdresse = ""
BewerbugnsOrt = ""
Email = ""

while True:
    Firma = input("Firma: ")
    BewerbugnsAdresse = input("Bewerbungsadresse: ")
    BewerbugnsOrt = input("Bewerbungsemail: ")
    Email = input("Email: ")
    if not Firma or not BewerbugnsAdresse or not BewerbugnsOrt or not Email:
        print("Bitte alles eingeben.")
    else:
        print("changing files..")
        waiting_animation(3)
        wordchanger("Bewerbungsvorlage.docx", "Firma", Firma)

