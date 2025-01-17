'''
Operacje na listach:

- dodawanie elementów
- usuwanie elementów
'''

cars = [
    "Toyota",
    "Ford",
    "BMW",
    "Mercedes",
    "Honda"
]

print(cars)

cars.append("Tesla") # Dodaj nowy samochód

print(cars)

cars.append("Polonez") # I kolejny

print(cars)

cars.pop() # Usuń ostatni element

print(cars)

cars.remove('BMW') # Usuń BMW

print(cars)

cars.pop(1) # Usuń drugi element listy (Ford)

print(cars)

cars.insert(1, "Fiat") # Dodaj na drugą pozycję markę 'Fiat'

print(cars)


