'''
Zapisz obiekt "Osoba" do pliku "Program9 - json/program9_a.json"
'''

import json

class Osoba:
    def __init__(self, imie, wiek, miasto):
        self.imie = imie
        self.wiek = wiek
        self.miasto = miasto

    # Metoda do konwersji obiektu na słownik
    def to_dict(self):
        return {
            'imie': self.imie,
            'wiek': self.wiek,
            'miasto': self.miasto
        }

# Tworzymy obiekt
osoba = Osoba("Jan", 30, "Warszawa")

with open("Program9 - json/program9_a.json", 'w') as f:
    json.dump(osoba.to_dict(), f, indent=4)