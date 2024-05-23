# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand

# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    """ Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
    alternativt modifiera respektive attribut. """
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Det här är {self.namn}. Hen är {self.ålder} år gammal."

    # Setters
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    # Getters
    def getNamn(self):
        return self.namn

    def getÅlder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #

# Lägger till en ny person i bussen.
def plockaUpp(passagerare):
    if len(passagerare) >= 25:
        print("Bussen är full. Ny passagerare kan inte stiga på.")
        return
    namn = input("Ange passagerarens namn: ")
    ålder = int(input("Ange passagerarens ålder: "))
    passagerare.append(Person(namn, ålder))
    print(f"{namn} har plockats upp och är nu ombord på bussen.")

# Avlägsnar en person från bussen.
def gåAv(passagerare):
    if not passagerare:
        print("Det finns inga passagerare att låta gå av.")
        return

    print("Vilken passagerare vill du låta gå av? Ange numret på passageraren.")
    for i, person in enumerate(passagerare):
        print(f"{i+1}. {person.getNamn()} ({person.getÅlder()} år)")

    val = input("-> ")
    try:
        val = int(val)
        if val < 1 or val > len(passagerare):
            print("Ogiltigt val. Försök igen.")
            return
        avlägsnad_person = passagerare.pop(val - 1)
        print(f"{avlägsnad_person.getNamn()} har lämnat bussen.")
    except ValueError:
        print("Felaktigt inmatning. Vänligen ange ett nummer.")

# Listar alla passagerare på bussen.
def skrivUt(passagerare):
    if not passagerare:
        print("Det finns inga passagerare på bussen.")
        return
    print("Passagerare på bussen:")
    for person in passagerare:
        print(person)

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagdÅlder(passagerare):
    total_ålder = sum(person.getÅlder() for person in passagerare)
    print(f"Den sammanlagda åldern på passagerarna är {total_ålder} år.")

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder(passagerare):
    if not passagerare:
        print("Det finns inga passagerare på bussen.")
        return
    total_ålder = sum(person.getÅlder() for person in passagerare)
    medel_ålder = total_ålder / len(passagerare)
    print(f"Medelåldern på passagerarna är {medel_ålder:.2f} år.")

# Skriver ut personen som är äldst på bussen.
def äldst(passagerare):
    if not passagerare:
        print("Det finns inga passagerare på bussen.")
        return
    äldst_person = max(passagerare, key=lambda person: person.getÅlder())
    print(f"{äldst_person.getNamn()} är den äldsta personen på bussen, {äldst_person.getÅlder()} år gammal.")

# Sorterar bussen efter namn.
def busSortNamn(passagerare):
    passagerare.sort(key=lambda person: person.getNamn())
    print("Bussen har sorterats efter namn.")

# Sorterar bussen efter namn.
def busSortNamn(passagerare):
    passagerare.sort(key=lambda person: person.getNamn())
    print("Bussen har sorterats efter namn.")

# Sorterar bussen efter ålder.
def busSortÅlder(passagerare):
    passagerare.sort(key=lambda person: person.getÅlder())
    print("Bussen har sorterats efter ålder.")

# Sorterar bussen.
def busSort(passagerare):
    print("Hur vill du sortera bussen? Ange 'n' för namn eller 'å' för ålder:")
    val = input("-> ")
    if val.lower() == 'n':
        busSortNamn(passagerare)
    elif val.lower() == 'å':
        busSortÅlder(passagerare)
    else:
        print("Ogiltigt val. Försök igen.")

# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare(passagerare):
    print("Ange det lägsta åldersvärdet i spannet:")
    lägsta_ålder = int(input("-> "))
    print("Ange det högsta åldersvärdet i spannet:")
    högsta_ålder = int(input("-> "))
    åldersSpann = (lägsta_ålder, högsta_ålder)
    hittaPassagerareInomSpann(åldersSpann, passagerare)

# Funktion för att söka passagerare inom ett specifikt åldersspann.
def hittaPassagerareInomSpann(åldersSpann, passagerare):
    lägsta_ålder, högsta_ålder = åldersSpann
    passagerare_inom_spann = [person for person in passagerare if lägsta_ålder <= person.getÅlder() <= högsta_ålder]
    if passagerare_inom_spann:
        print("Passagerare inom det angivna åldersspannet:")
        for person in passagerare_inom_spann:
            print(person)
    else:
        print("Det finns inga passagerare inom det angivna åldersspannet.")

# Peta på passagerare.
def peta(passagerare):
    if not passagerare:
        print("Det finns inga passagerare på bussen att peta på.")
        return

    petad_person = rand.choice(passagerare)
    reaktioner = {
        "barn": ["Aj! Det gjorde ont!", "Hej, sluta peta!"],
        "vuxen": ["Vad gör du?", "Var försiktig!"],
        "äldre": ["Ursäkta, men vad gör du?", "Snälla sluta."],
    }

    ålder = petad_person.getÅlder()
    if ålder < 18:
        reaktion = rand.choice(reaktioner["barn"])
    elif 18 <= ålder < 65:
        reaktion = rand.choice(reaktioner["vuxen"])
    else:
        reaktion = rand.choice(reaktioner["äldre"])

    print(f"{petad_person.getNamn()} reagerar: {reaktion}")

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    passagerare = []

    print(
    """
                                           _____________
                                         _/_|[][][][][] | - -
                                        (     Bussen    | - -
                                        =--OO-------OO--=
    """)

    while True:
        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                               q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            plockaUpp(passagerare)
        elif menyVal == "2":
            gåAv(passagerare)
        elif menyVal == "3":
            skrivUt(passagerare)
        elif menyVal == "4":
            sammanlagdÅlder(passagerare)
        elif menyVal == "5":
            medelÅlder(passagerare)
        elif menyVal == "6":
            äldst(passagerare)
        elif menyVal == "7":
            busSort(passagerare)
        elif menyVal == "8":
            hittaPassagerare(passagerare)
        elif menyVal == "9":
            peta(passagerare)
        elif menyVal.lower() == "q":
            print("Programmet avslutas.")
            break
        else:
            print("Ogiltigt val. Försök igen.")

if __name__ == "__main__":
    main()