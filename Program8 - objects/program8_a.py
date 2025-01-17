'''
Utwórz klasę (obiekt) Gracz zawierający następujące pola:

    - Imię
    - Pozycja np. napastnik, obrońca
    - Numer
    
Dodaj następujące metody (funkcje):

    - biegaj - metoda wyświetla następujący tekst: "<imię> biegnie po boisku!"
    - strzelaj - metoda wyświetla następujący tekst: "<imię> strzela z pozycji <pozycja>!"
    - opis - metoda wyświetla opis gracza: "Imię: <imię>, Pozycja: <pozycja>, Numer: <numer>"
'''

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
        
        
# Tworzenie obiektów (graczy)
gracz1 = Gracz("Robert Lewandowski", "napastnik", 7)
gracz2 = Gracz("Kamil Glik", "obrońca", 5)


print(gracz1.imie)
print(gracz2.pozycja)


# Wywołanie metod
gracz1.biegaj()  # Robert Lewandowski biegnie po boisku!
gracz1.opis()

gracz2.strzelaj()  # Kamil Glik strzela na bramkę!
gracz2.opis()