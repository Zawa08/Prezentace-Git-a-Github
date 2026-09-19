"""
ŽÁKOVSKÁ KNÍŽKA – hlavní program (HOTOVÝ, neupravujte)
Spuštění:  python main.py
Dokud funkce nejsou hotové, vypisují ???
"""
from znamky import prumer, prospel
from test import body_na_znamku, slovne

jmeno = "Adam"
znamky = [1, 2, 1, 3, 2]
body_z_testu = 72

print("Žák:", jmeno)
print("Známky:", znamky)
print("Průměr:", prumer(znamky))
print("Prospěl:", prospel(znamky))
print()
znamka = body_na_znamku(body_z_testu)
print("Test:", body_z_testu, "bodů")
print("Známka z testu:", znamka)
print("Slovně:", slovne(znamka))
