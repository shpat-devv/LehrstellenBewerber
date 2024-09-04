import time

while True:
    print("""Wozu brauchst du hilfe?
    1. Google Account machen mit passkey (nötig)
    2. Was soll ich and der Bewerbung ändern?
    3. Wo gebe ich die nötigen Benutzerdaten ein für mein Google Konto?
    4. Wo füge ich Dateien hinzu?
    5. Nichts, ich brauche keine Hilfe.
    Wähle eine Nummer aus:""")

    user_input = input("Wähle eine Nummer aus: ")

    if user_input == "1":
        print("Geh in deinen Google Konto eintellungen, Schalte 2fa an. Dannach gebe in deiner Searchbar diesen link ein  https://myaccount.google.com/apppasswords, Krier dort dein Eigenes Passkey und merk es dir :)")
    
    elif user_input == "2":
        print("Im ordner Bewerbung findest du eine word datei namens Bewerbung.docx, dort kannst du deine Bewerbung anpassen. Ändere deine Personal Daten, Und den Unteren Text, Lass die Komischen Buchstaben so wie sie sind, die werden später ersetzt.")
    
    elif user_input == "3":
        print("Erstelle eine Datei namens secret.py am gleichen Platz wo das Main Program liegt, und füge folgendes ein: \nsecretgooglekey = dein key \ngoogleemail = dein google mail")

    elif user_input == "4":
        print("Im Ordner Bewerbung/tosend kannst du deine Dateien hinzufügen, die werden dann automatisch in die Email hinzugefügt. Pass auf das die Datei nicht zu gross ist")
    
    elif user_input == "5":
        print("Okay, viel Erfolg bei deiner Bewerbung!")

    else:
        print("Bitte wähle eine Nummer aus.")
        continue

    time.sleep(3)

