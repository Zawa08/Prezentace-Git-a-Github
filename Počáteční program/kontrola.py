# Rychlá kontrola:  python kontrola.py
from znamky import prumer, prospel
from test import body_na_znamku, slovne

def over(nazev, vysledek, spravne):
    if vysledek == spravne:
        print("OK     ", nazev)
    else:
        print("CHYBA  ", nazev, "-> vyšlo", vysledek, ", mělo vyjít", spravne)

over("A1 prumer", prumer([1, 2, 3]), 2.0)
over("A2 prospel bez pětky", prospel([1, 2, 4]), True)
over("A2 prospel s pětkou", prospel([1, 5, 2]), False)
over("B1 body 95", body_na_znamku(95), 1)
over("B1 body 72", body_na_znamku(72), 3)
over("B1 body 10", body_na_znamku(10), 5)
over("B2 slovne 1", slovne(1), "výborně")
over("B2 slovne 5", slovne(5), "nedostatečně")
