from gracz import Gracz
from mecz import Mecz
import jsonpickle

gracz1 = Gracz("Robert Lewandowski", "napastnik", 7)
gracz2 = Gracz("Kamil Glik", "obrońca", 5)

mecz = Mecz("FC Barcelona", "Real Madryt")
mecz.dodaj_gracza(gracz1)
mecz.dodaj_gracza(gracz2)

with open("Program9 - json/program9_b.json", 'w') as f:
    jsonpickle.dump(mecz, f)

