'''
Nieskoczona pętla.

Napisz program, który będzie wypisywał wpisane przez użytkownika słowo dopóki użytkownik nie wpisze słowa "stop".
'''

while True:
    dane = input("Podaj dowolny tekst (wpisz 'stop', aby zakończyć): ")
    if dane.lower() == "stop":
        print("Koniec programu.")
        break
    print(f"Wpisałeś: {dane}")