'''
1. Wprowadzenie:
    Stwórz program, który będzie zarządzał prostą biblioteką książek. Program powinien umożliwiać:

    - Dodawanie nowych książek.
    - Wyświetlanie wszystkich zapisanych książek.
    - Wyszukiwanie książki po tytule.

2. Szczegóły techniczne:

    - Wszystkie dane o książkach (np. tytuł i autor) powinny być zapisywane w pliku tekstowym books.txt.
    - Każda książka powinna zajmować jedną linię w formacie: Tytuł - Autor
    - Po uruchomieniu program powinien odczytać plik, aby załadować istniejące książki do listy.
    
3. Funkcjonalności programu:

    - Dodawanie książki: Użytkownik podaje tytuł i autora, które są zapisywane do pliku.
    - Wyświetlanie książek: Program odczytuje wszystkie książki z pliku i wyświetla je.
    - Wyszukiwanie książki: Użytkownik podaje tytuł, a program sprawdza, czy dana książka znajduje się w pliku. Jeśli tak, wyświetla jej szczegóły.

Przykładowy użycie programu:

    Witaj w bibliotece!
    1. Dodaj książkę
    2. Wyświetl wszystkie książki
    3. Wyszukaj książkę
    4. Wyjście

    Wybierz opcję: 1
    Podaj tytuł książki: W pustyni i w puszczy
    Podaj autora książki: Henryk Sienkiewicz
    Książka została dodana!

    Wybierz opcję: 2
    Lista książek:
    1. W pustyni i w puszczy - Henryk Sienkiewicz

    Wybierz opcję: 3
    Podaj tytuł książki: W pust
    Znaleziono książkę: W pustyni i w puszczy - Henryk Sienkiewicz
    
    Wybierz opcję: 3
    Podaj tytuł książki: Lalka
    Nie znaleziono książki


Podpowiedzi:

1. Do wczytywania książek z pliku do listy i zapisywania książek z listy do pliku warto zastosować
    wczytywanie / zapisywanie linia po linii
    
    Przykład:
    
    my_list = [1, 2, 3, 4, 5]
    with open("output.txt", "w") as file:
        for item in my_list:
            file.write(item + \n")

2. Do wyszukiwania książek warto użyć operatora "in", który sprawdza czy dany string zawiera wybraną
    frazę. 
    
    Przykład:
    
    tekst = "To jest przykładowy tekst."
    fraza = "przykładowy"

    if fraza in tekst:
        print("Fraza została znaleziona!")
    else:
        print("Fraza nie została znaleziona.")

'''