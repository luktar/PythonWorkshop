
'''
Napisz program do sumowania liczb od 1 do 5 przy użyciu pętli while.
'''

sum_of_numbers = 0  # Zmienna przechowująca sumę
number = 1          # Pierwsza liczba do sumowania

# Pętla while sumująca liczby od 1 do 5
while number <= 5:
    sum_of_numbers += number  # Dodanie liczby do sumy
    number += 1               # Przejście do następnej liczby

print("Suma liczb od 1 do 5 wynosi:", sum_of_numbers)