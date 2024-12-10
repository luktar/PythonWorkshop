'''
Napisz program, który po wpisaniu wieku poinformuje użytkownika, czy powinien być na diecie, czy nie.
Jeżeli użytkownik ma mniej niż 30 lat to nie musi być na diecie, a jak ma więcej to musi.
'''

print("Diet Coach App")

age = input("Enter your age: ")

age = int(age)

if(age < 30):
    print("You can eat everything!")
else:
    print("Start the diet immediately.")