'''
Dodatkowe operacje na listach:

- sprawdzenie długości
- sortowanie
- odwrócenie kolejności
'''

cars = [
    "Toyota",
    "Ford",
    "BMW",
    "Mercedes",
    "Honda"
]

print(cars)

print("Lenght: " + str(len(cars)))

# Add 3 elements
cars.append("Polonez")
cars.append("Tesla")
cars.append("Fiat")

print("Lenght: " + str(len(cars)))

# Odwrócenie kolejności elementów w liście

print("Before reverse: " + str(cars))
cars.reverse()
print("After reverse: " + str(cars))

# Sortowanie

print("Before sort: " + str(cars))
cars.sort()
print("After sort: " + str(cars))
