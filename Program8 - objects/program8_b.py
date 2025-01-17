'''
Utwórz obiekt Mecz zawierający następujące pola:
    - goscie - nazwa zespołu gości
    - gospodarze - nazwa zespołu gospodarzy
    - gracze - lista zawierająca obiekty typu Gracz
    
W klasie Mecz utwórz następujące metody:
    - "dodaj_gracza(gracz)" pozwala na dodania gracza do listy graczy.
    - "wyswietl_graczy()" wyświetla szczegóły meczu w następujący sposób
    
Gracze w meczu <gospodarze> vs <goscie>
Imię: <imie>, Pozycja: <pozycja>, Numer: <numer>
Imię: <imie>, Pozycja: <pozycja>, Numer: <numer>
Imię: <imie>, Pozycja: <pozycja>, Numer: <numer>
Imię: <imie>, Pozycja: <pozycja>, Numer: <numer>

Informacja:

Klasa "Gracz" została przeniesiona do osobnego pliku o nazwie "gracz.py" oraz zaimporotowana za pomocą metody "from gracz import Gracz".
W osobnym pliku została również utworzona klasa Mecz (mecz.py) oraz zaimportowana w identyczny sposób.
'''

from gracz import Gracz
from mecz import Mecz

gracz1 = Gracz("Robert Lewandowski", "napastnik", 7)
gracz2 = Gracz("Kamil Glik", "obrońca", 5)

mecz = Mecz("FC Barcelona", "Real Madryt")
mecz.dodaj_gracza(gracz1)
mecz.dodaj_gracza(gracz2)

mecz.wyswietl_graczy()

