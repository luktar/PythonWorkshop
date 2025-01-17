'''
Wypisz wszsytkie liczby z listy na różne sposoby.
'''

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# Wypisz wszystkie elementy listy
print(numbers)

print(str(numbers[3]))

# Wypisz wszystkie elementy listy za pomocą pętli
for i in numbers:
    print(i)
    
# Wypisz wszystkie elementy listy jeden pod drugim wraz z numerem indeksu
# Sposób 1 - inkrementacja indeksu
index = 0
for i in numbers:
    print('Index: ' + str(index) + ", Value: " + str(i))
    index += 1
    
# Sposób 2 - enumerator
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")
    
