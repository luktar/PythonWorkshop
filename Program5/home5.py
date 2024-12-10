'''
Zadanie domowe: Zarządzanie listą książek w bibliotece
Napisz program, który pozwala zarządzać listą książek w małej bibliotece. Program powinien oferować użytkownikowi następujące funkcje:

- Dodanie książki: Użytkownik podaje tytuł książki, która zostaje dodana do listy. Sprawdź, czy książka już istnieje w liście, zanim ją dodasz.
- Usunięcie książki: Użytkownik podaje tytuł książki do usunięcia. Jeśli książka istnieje na liście, usuń ją, w przeciwnym razie wyświetl odpowiedni komunikat.
- Wyświetlenie listy książek w porządku alfabetycznym: Posortuj listę i wypisz wszystkie książki.
- Odwrócenie kolejności książek: Wyświetl listę książek w odwrotnej kolejności.
- Sprawdzenie, czy książka jest na liście: Użytkownik podaje tytuł książki, a program sprawdza, czy książka znajduje się na liście.

Przykład działania programu:

# 1

Co chcesz zrobić? [add/remove/show/sort/reverse/check]: add
Podaj tytuł książki: Władca Pierścieni
Książka została dodana.

# 2

Co chcesz zrobić? [add/remove/show/sort/reverse/check]: add
Podaj tytuł książki: Hobbit
Książka została dodana.

# 3

Co chcesz zrobić? [add/remove/show/sort/reverse/check]: show
Lista książek: ['Władca Pierścieni', 'Hobbit']

# 4

Co chcesz zrobić? [add/remove/show/sort/reverse/check]: sort
Lista książek (posortowana): ['Hobbit', 'Władca Pierścieni']

# 5

Co chcesz zrobić? [add/remove/show/sort/reverse/check]: reverse
Lista książek (odwrócona): ['Władca Pierścieni', 'Hobbit']

# 6

Co chcesz zrobić? [add/remove/show/sort/reverse/check]: check
Podaj tytuł książki: Hobbit
Książka znajduje się na liście.

'''