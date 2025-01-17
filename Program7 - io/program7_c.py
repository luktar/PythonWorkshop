'''
Przeczytaj zawartość pliku zlokalizowanego pod ścieżką "Program7 - io/program7_c.txt"
'''

with open("Program7 - io/program7_c.txt", "r") as file:
    content = file.read()
    print(content)