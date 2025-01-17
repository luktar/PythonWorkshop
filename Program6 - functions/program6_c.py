'''
Zwracanie wartości funkcji.

Napisz funkcję, która dodaje dwie liczby.

Następnie napisz funkcję, która sumuje liczby od 0 do 9 w nasępujący sposób:
0 + 0 = 0
1 + 1 = 2
2 + 2 = 4
...
9 + 9 = 18
'''

def dodaj(a, b):
    return a + b

result = dodaj(3, 5)
print(result)

for i in range(10):
    a = dodaj(i, i)
    print(str(i) + " + " + str(i) + " = " + str(a))

