class Gracz:
    def __init__(self, imie, pozycja, numer):
        self.imie = imie
        self.pozycja = pozycja
        self.numer = numer

    def biegaj(self):
        print(f"{self.imie} biegnie po boisku!")

    def strzelaj(self):
        print(self.imie + " strzela z pozycji " + self.pozycja + "!")
        
    def opis(self):
        print("Imię: " + self.imie + ", Pozycja: " + self.pozycja + ", Numer: " + str(self.numer))