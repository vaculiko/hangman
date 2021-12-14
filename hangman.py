import os
from random import choice, seed
from slova import hadana_slova
from grafika import obesenec

zivoty = 7
hra_bezi = True
# slovo = "obesenec" # TODO: Náhodný výběr slov pomocí random.choice()
# zafixuji nahodny vyber
# seed(42)
slovo = choice(hadana_slova)
tajenka = len(slovo) * ["_"]
hadana_pismena = []
oznameni = ''

# 1. Smyčka pro celou hru, hlídání životů
while hra_bezi and zivoty > 0:
    os.system("cls")
    print(f"Tajenka: {''.join(tajenka)}")
    print(obesenec[7 - zivoty])
    print(oznameni)
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
        for index, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[index] = hadani
        oznameni = 'Uhodl jsi pismeno!'
        if "_" not in tajenka:
            hra_bezi = False
    # zadane slovo ani pismeno neni v tajence
    else:
        hadana_pismena.append(hadani)
        zivoty = zivoty - 1
        oznameni = "Chybka!"
# 3. Vyhodnocení výsledku hry
else:
    # slovo je uhadnute
    if hra_bezi == False:
        os.system("cls")
        print(f"Tajenka: {slovo}", "Gratulujeme, vyhráli jste!", sep='\n')
    # dosly zivoty
    else:
        os.system("cls")
        print(f"Prohrál jsi, tajenka byla {slovo}")
        print(obesenec[7 - zivoty])

