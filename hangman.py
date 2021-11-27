import getpass
import time

# 1 Willkommenstext
begrueßung = """Herzlich Willkommen zu Hangman!
"""
print(begrueßung)

# 2 Suchwort in einer Variable festhalten
suchwort = getpass.getpass('Spieler 1: Geben Sie ihr Wort ein:')
suchwort_groß = suchwort.upper()
time.sleep(1)

# 2a Das Suchwort Verdeckt anzeigen

anzahl_buchstaben_suchwort = len(suchwort_groß)

satzohnebuchstaben = f"_"*anzahl_buchstaben_suchwort

print(satzohnebuchstaben)

satzmitbuchstaben = f": "

# 5 Den Buchstaben an der richtigen Stelle ersetzen

satzohnebuchstaben_liste = list(satzohnebuchstaben)

suchwort_groß_liste = list(suchwort_groß)

ping = 0

neuer_string = ""

while ping < 6:
    if ping == 1:
        print("""
            ┴
        """)
    if ping == 2:
        print("""
                |
                |
                |
                A""")
    if ping == 3:
        print("""
                _____
                |   |
                |  
                |   
                |   
                ┴""")
    if ping == 4:
        print("""
                _____
                |   |
                |   O
                |   ┼ 
                |   ^
                ┴""")
    if ping == 5:
        print("""
                _____
                |   |
                |  \o⁄
                |   I   
                |   A
                ┴""")
    if neuer_string == suchwort_groß:
        print(f"Super du hast mit {ping} Fehlversuch(en) gewonnen!")
        break
    if ping == 4:
        print("Come on Bro, Du hast nur noch einen Versuch!")
    if ping == 5:
        print(f"Du bist wohl zu blöd?! Das Richtige Wort war \"{suchwort}\"")
        break
    print("Einen neuen Buchstaben eingeben")
    buchstabe = input()
    buchstabe_groß = buchstabe.upper()
    ticker = 0
    neuer_string = ""
    benutzte_buchstaben = ""
    if buchstabe_groß in suchwort_groß:
        print(f"Der Buchstabe {buchstabe_groß} ist enthalten")
        time.sleep(1)
    else:
        ping = ping + 1
        print(f"Der Buchstabe {buchstabe_groß} ist nicht enthalten")
        time.sleep(1)
    for letter in suchwort_groß_liste:
        if letter == buchstabe_groß:
            satzohnebuchstaben_liste[ticker] = buchstabe_groß
        ticker = ticker + 1
        neuer_string = "".join(satzohnebuchstaben_liste)
    else:
        ticker = ticker + 1
        satzmitbuchstaben = satzmitbuchstaben + buchstabe_groß
        print("   " + neuer_string + "   " + "|| Benutzte Buchstaben " +
              satzmitbuchstaben + " ")
