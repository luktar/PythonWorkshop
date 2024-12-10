'''
Napisz program, który:

Pyta użytkownika o liczbę zdobytych punktów (liczba całkowita).
Na podstawie punktów wyświetla ocenę:
- Jeśli punkty są mniejsze niż 50: "You need more practice!"
- Jeśli punkty wynoszą od 50 do 80: "Good job, keep going!"
- Jeśli punkty wynoszą powyżej 80: "Excellent! You're a pro!"
'''

points = input("Enter your game score: ")
points = int(points) # convert to integer

if points < 50:
    print("You need more practice!")
elif 50 <= points <= 80:
    print("Good job, keep going!")
else:
    print("Excellent! You're a pro!")