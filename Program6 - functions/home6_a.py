'''
Zadanie domowe: Prosty system oceniania
Stwórz program, który pozwala użytkownikowi wprowadzić listę ocen (np. szkolnych) i 
wylicza ich średnią. Program ma spełniać poniższe wymagania:

1. Pobierz dane od użytkownika:

    - Pobiera oceny od użytkownika w pętli (użytkownik wpisuje kolejne liczby) i zapisz je w liście.
    - Zakończ wprowadzanie ocen po wpisaniu wartości -1.
    - Zwróć listę wprowadzonych ocen.

2. Napisz funkcję oblicz_srednia(oceny), która:

    - Przyjmuje listę ocen jako argument.
    - Zwraca średnią arytmetyczną ocen.
    - Jeśli lista jest pusta, zwraca komunikat: "Brak ocen do obliczenia średniej.".
    - parametr "oceny" jest typu lista

3. Napisz funkcję klasyfikacja(srednia), która na podstawie średniej zwraca ocenę końcową w formie tekstowej:

    - Średnia >= 4.5: "Bardzo dobry".
    - Średnia >= 3.5: "Dobry".
    - Średnia >= 2.5: "Dostateczny".
    - Średnia < 2.5: "Niedostateczny".
    
Podaj oceny (wpisz -1, aby zakończyć):
> 4
> 5
> 3
> -1

Wprowadzone oceny: [4, 5, 3]
Średnia ocen: 4.0
Ocena końcowa: Dobry


Dla chętnych:
Dodaj walidację wprowadzanych danych, aby program akceptował tylko liczby z zakresu od 1 do 5. 
W przypadku nieprawidłowego wejścia wyświetl komunikat: "Nieprawidłowa ocena, podaj wartość od 1 do 5.".
'''