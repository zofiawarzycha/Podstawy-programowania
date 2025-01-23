'''Napisać funkcję polacz_listy, która przyjmuje dowolną liczbę list i zwraca jedną połączoną listę bez
duplikatów zawierającą wszystkie elementy z podanych list. Wykorzystać funkcję z argumentem
wielowartościowym. Listy mają być podane bezpośrednio w kodzie. '''

from itertools import chain

def polacz_listy(*listy):
    return list(set(chain(*listy)))

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
lista3 = [6, 7, 8]
wynik = polacz_listy(lista1, lista2, lista3)
print("Połączona lista bez duplikatów:", wynik)

