'''
Napisz program, który zapisuje imię do pliku "Program7_a.txt" w folderze "Program7 - io".
'''

name = input("Podaj swoje imię: ")

with open("Program7 - io/Program7_a.txt", "a") as file:
    file.write(name + "\n")

print("Imię zapisano do pliku.")