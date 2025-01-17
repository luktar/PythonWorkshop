'''
Napisz program, który zapisuje do pliku liczby od 1 do 1000.
Ścieżka do pliku: "Program7 - io/program7_b.txt".
'''

with open("Program7 - io/program7_b.txt", "w") as file:
    for number in range(1, 1001):
        file.write(number + "\n")