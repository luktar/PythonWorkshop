class Mecz:
    def __init__(self, gospodarze, goscie):
        self.gospodarze = gospodarze  # Nazwa gospodarzy
        self.goscie = goscie # Nazwa gosci
        self.gracze = []  # Lista graczy w meczu

    def dodaj_gracza(self, gracz):
        self.gracze.append(gracz)  # Dodanie gracza do listy

    def wyswietl_graczy(self):
        print("Gracze w meczu " + self.gospodarze + " vs " + self.goscie)
        for gracz in self.gracze:
            print("Imię: " + gracz.imie + ", Pozycja: " + gracz.pozycja + ", Numer: " + str(gracz.numer))