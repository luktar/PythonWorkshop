'''
Sprawdzenie, czy lista zawiera wybrany element.
'''

cities = [
    "New York",
    "London",
    "Tokyo",
    "Paris",
    "Berlin",
    "Sydney",
    "Rome",
    "Barcelona",
    "Toronto",
    "Dubai"
]

city_name = input("Insert city name: ")

if(city_name in cities):
    print("City " + city_name + " is in the list.")
else:
    print("There is no city " + city_name + " on the list.")