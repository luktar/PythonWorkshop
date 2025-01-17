'''
Zadanie domowe: Gra w zgadywanie liczb
Napisz program, który pozwoli użytkownikowi zagrać w prostą grę w zgadywanie liczb. Program powinien wykorzystywać funkcje, instrukcje warunkowe, pętle oraz listy.

Główne wymagania:

1. Funkcja losuj_liczbe()

    - Generuje losową liczbę z zakresu 1–100 i zwraca ją.
    - do wygenerowania liczby losowej od 1 do 100 możesz użyć funkcji: random.randint(1, 100)

2. Funkcja zgaduj_liczbe(wylosowana_liczba)

    - Umożliwia użytkownikowi wielokrotne zgadywanie liczby w pętli:
        Po każdym zgadywaniu informuje, czy liczba jest za duża, za mała, czy poprawna.
        Dodaje każdą próbę użytkownika do listy.
    - Kończy działanie, gdy użytkownik zgadnie liczbę, i zwraca listę wszystkich prób.

3. Funkcja podsumowanie(proby)

    - Wyświetla podsumowanie gry, w tym:
    - Liczbę prób.
    - Listę wszystkich zgadywanych liczb.

Przykładowe działanie programu:

Zgadnij liczbę (od 1 do 100):
> 50
Za duża! Spróbuj ponownie.
> 25
Za mała! Spróbuj ponownie.
> 37
Gratulacje! Zgadłeś.

Podsumowanie:
Liczba prób: 3
Twoje zgadywania: [50, 25, 37]
'''