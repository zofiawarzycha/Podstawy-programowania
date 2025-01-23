'''
Napisać program, w którym należy sprawdzić we funkcji, czy podana liczba jest liczbą doskonała. Liczba
doskonała to liczba naturalna, która jest sumą wszystkich swych naturalnych dzielników właściwych
(to znaczy od niej mniejszych).
'''
def jest_doskonala():
    liczba = int(input("Podaj liczbę, którą chcesz sprawdzić pod względem doskonałości: "))

    suma_dzielnikow = 0
    for i in range(1, liczba):
        if liczba % i == 0:
            suma_dzielnikow += i

    if suma_dzielnikow == liczba:
        print(f"Liczba {liczba} jest liczbą doskonałą.")
    else:
        print(f"Liczba {liczba} nie jest liczbą doskonałą.")

jest_doskonala()


