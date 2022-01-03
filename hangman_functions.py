import os
from random import choice, seed
from slova import hadana_slova
from grafika import obesenec

def hra():
    """Spusti beh hry obesenec."""
    slovo = choice(hadana_slova)
    tajenka = len(slovo) * ["_"]
    print("Hrajeme!")

def zobraz_stav_hry():
    """Vycisti konzoli a vykresli obesence s tajenkou."""
    pass

def je_pismeno_ve_slove():
    """Vraci index pismena, pokud je nalezeno ve slove."""
    pass

def prepis_pismeno():
    """Prepise uhadnuta pismena v tajence."""
    pass

def kompletni_tajenka():
    """Kontrola, zda je slovo uhadnute."""
    pass

def konec_hry():
    """Vypis na konci hry."""
    pass

# Jeden beh hry
hra()

# TODO: Cyklus pro opakovane hrani