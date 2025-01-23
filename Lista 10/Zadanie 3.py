'''
Napisać program, w którym należy wygenerować za pomocą wyrażania generującego nieparzyste
liczby pierwsze od 1 do 100. Sprawdzanie, czy liczba jest pierwsza powinno odbyć się we funkcji.
'''
def jest_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

nieparzyste_liczby_pierwsze = (x for x in range(1, 101) if x % 2 != 0 and jest_pierwsza(x))

for liczba in nieparzyste_liczby_pierwsze:
    print(liczba)
