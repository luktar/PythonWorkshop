'''
Zadanie domowe: "System zarządzania zadaniami w projekcie"

1. Klasa Zadanie:

    Każde zadanie w projekcie ma następujące atrybuty:
    
        - nazwa – nazwa zadania (typ: string, np. "Przygotowanie raportu").
        - opis – krótki opis zadania (typ: string).
        - status – status zadania (np. "do zrobienia", "w trakcie", "zakończone").
        - priorytet – priorytet zadania (np. "wysoki", "średni", "niski").
        - termin – termin wykonania zadania (typ: string, np. "2025-02-15").
    
    Klasa powinna zawierać dwie metody:

        - aktualizuj_status(nowy_status), która pozwala na zaktualizowanie statusu zadania.
        - wyswietl_info(), która wyświetla informacje o zadaniu w czytelny sposób.
        
2. Klasa Projekt:

    Klasa ta reprezentuje cały projekt. Projekt ma atrybut:
    
        - nazwa – nazwa projektu (np. "Projekt A").
        - zadania – lista zadań w projekcie (lista obiektów typu Zadanie).
        
    Klasa powinna mieć następujące metody:

        - dodaj_zadanie(zadanie), która pozwala dodać nowe zadanie do listy.
        - wyswietl_zadania(), która wyświetla wszystkie zadania w projekcie.
        - wyszukaj_zadania_po_statusie(status), która pozwala wyszukiwać zadania o określonym statusie.
        
Program nie musi mieć interfejsu użytkownika. Wystarczy, że w kodzie źródłowym utworzysz kilka
zadań oraz dodasz je do projektu.
Dodatkowo spróbuj zmienić status za pomocąmeody "aktualizuj_status(nowy_status)" w utworzonym obiekcie "Zadanie".

        
Przykładowe działanie programu:

Zadania w projekcie Projekt A:
Nazwa zadania: Przygotowanie raportu, Status: do zrobienia, Priorytet: wysoki, Termin: 2025-02-15
Opis: Przygotowanie raportu na koniec miesiąca
------------------------------
Nazwa zadania: Spotkanie z klientem, Status: w trakcie, Priorytet: średni, Termin: 2025-01-20
Opis: Omówienie wymagań projektu
------------------------------
Nazwa zadania: Analiza danych, Status: zakończone, Priorytet: niski, Termin: 2025-01-05
Opis: Analiza wyników badań
------------------------------
Zadania o statusie w trakcie:
Nazwa zadania: Spotkanie z klientem, Status: w trakcie, Priorytet: średni, Termin: 2025-01-20
Opis: Omówienie wymagań projektu
------------------------------
'''