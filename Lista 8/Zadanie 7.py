'''
Napisać program który wypisze na ekranie wszystkie możliwe kombinacje książek jakie można wybrać.
Do wyboru jest pięć książek, a wybieramy trzy z nich. Fragment danych jakie powinny zostać
wypisywane na ekranie:
1 2 3
1 2 4
1 2 5
'''
import itertools

def wypisz_kombinacje():
    ksiazki = [1, 2, 3, 4, 5]
    kombinacje = itertools.combinations(ksiazki, 3)

    for kombinacja in kombinacje:
        print(*kombinacja)

wypisz_kombinacje()