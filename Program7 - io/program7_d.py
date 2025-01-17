'''
Utwórz program, który wczyta zawartość pliku "Program7 - io/program7_c.txt", zmieni słowo
Califormication na dowolne inne słowo wprowadzone przez użytkownika i zapisze nowy tekst do
pliku pod ścieżką "Program7 - io/program7_d.txt".

Wybrany tekst można zastąpić za pomocą funkcji "replace".

text = text.replace("Old phrase", "New phrase")

Przykład:

text = "Hello world. I like ice creams. Hello!"
text = text.replace("Hello", "Welcome")

Wynik:
"Welcome world. I like ice creams. Welcome!"
'''

# Funkcja read wczytuje plik "program7_c.txt" i zwraca jego zawartość
def read():
    content = ""
    with open("Program7 - io/program7_c.txt", "r") as file:
        content = file.read()
    return content

# Funkcja write zapisje zawartość parametru "text" do pliku "program7_d.txt"
def write(text):
    with open("Program7 - io/program7_d.txt", "w") as file:
        file.write(text)

text = read()

text = text.replace("Californication", "Katowice")

write(text)