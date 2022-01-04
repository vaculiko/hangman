import os
from random import choice, seed
from slova import hadana_slova
from grafika import obesenec

def hra():
    """Spusti beh hry obesenec."""
    #seed(42) # tajenka == pecka
    zivoty = 7
    hra_bezi = True
    slovo = choice(hadana_slova)
    tajenka = len(slovo) * ["_"]
    hadana_pismena = []
    oznameni = ''

    # 1. Smyčka pro celou hru, hlídání životů
    while hra_bezi and zivoty > 0:
        zobraz_stav_hry(tajenka, zivoty, oznameni)
        # 2. Hádání slova/písmena - input()
        hadani = input("Hadej pismeno/slovo:")

        # je zadane cele slovo stejne jako tajenka?
        if hadani == slovo:
            hra_bezi = False
        # neni pismeno v tajence? # TODO: rozsirit na seznam control
        elif hadani in hadana_pismena:
            oznameni = 'Pismeno uz jsi hadal!'
        # je zadane pismeno v tajence
        elif len(hadani) == 1 and hadani in slovo:
            hadana_pismena.append(hadani)
            indexy = je_pismeno_ve_slove(hadani, slovo)
            if indexy:
                tajenka = prepis_pismeno(tajenka, hadani, indexy)
            oznameni = 'Uhodl jsi pismeno!'

            hra_bezi = kompletni_tajenka(tajenka)
        # zadane slovo ani pismeno neni v tajence
        else:
            hadana_pismena.append(hadani)
            zivoty -= 1
            oznameni = "Chybka!"
    # 3. Vyhodnocení výsledku hry
    else:
        os.system("cls")
        konec_hry(zivoty, slovo)

def zobraz_stav_hry(tajenka, zivoty, oznameni):
    """Vycisti konzoli a vykresli obesence s tajenkou."""
    os.system("cls")
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(oznameni)

def je_pismeno_ve_slove(hadani, slovo):
    """Vraci index pismena, pokud je nalezeno ve slove."""
    return [
        index for index, pismeno in enumerate(slovo)
        if pismeno in hadani
    ]

def prepis_pismeno(tajenka, hadani, indexy):
    """Prepise uhadnuta pismena v tajence."""
    for index in indexy:
        tajenka[index] = hadani
    return tajenka

def kompletni_tajenka(tajenka):
    """Kontrola, zda je slovo uhadnute."""
    return False if "_" not in tajenka else True

def konec_hry(zivoty, slovo):
    """Vypis na konci hry."""
    if zivoty == 0:
        print(obesenec[7 - zivoty], f"Prohrál jsi, tajenka byla {slovo}.", sep='\n')
    else:
        print(f"Tajenka: {slovo}", "Gratulujeme, vyhráli jste!", sep='\n')

# Jeden beh hry
hra()

# TODO: Cyklus pro opakovane hrani