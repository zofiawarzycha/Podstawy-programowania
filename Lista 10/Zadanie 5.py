''' Napisać program z wykorzystaniem funkcji, który przeprowadzi operacje dodawania, odejmowania i
mnożenia dla dwóch podanych wielomianów. Dla każdego działania utworzyć osobną funkcję. Dla
dodawania i odejmowania dopasować długości wielomianów przez dodanie zer do krótszego
wielomianu. Wówczas wykorzystać funkcję zip. Funkcja zip(w1, w2) w Pythonie łączy elementy dwóch
iterowalnych obiektów w1 i w2 w pary. Tworzy sekwencję krotek, gdzie każdy element w parach składa
się z odpowiednio sparowanych elementów z w1 i w2. Na przykład:
w1 = [1, 2, 3]
w2 = ['a', 'b', 'c']
zipped = zip(w1, w2)
print(list(zipped))
[(1, 'a'), (2, 'b'), (3, 'c')]
W mnożeniu proszę zainicjalizować listę wynikową zerami.
wielomian_1 = [2, -3, 0, 4] # 2x**3 - 3x**2 + 4
wielomian_2 = [1, 5, 2] # x**2 + 5x + 2
Wyniki wyświetlić na ekranie komputera.
'''

def dodaj(wielomian_1, wielomian_2):
    dlugosc = max(len(wielomian_1), len(wielomian_2))
    wielomian_1 = [0] * (dlugosc - len(wielomian_1)) + wielomian_1
    wielomian_2 = [0] * (dlugosc - len(wielomian_2)) + wielomian_2

    wynik = [a + b for a, b in zip(wielomian_1, wielomian_2)]
    return wynik

def odejmij(wielomian_1, wielomian_2):
    dlugosc = max(len(wielomian_1), len(wielomian_2))
    wielomian_1 = [0] * (dlugosc - len(wielomian_1)) + wielomian_1
    wielomian_2 = [0] * (dlugosc - len(wielomian_2)) + wielomian_2

    wynik = [a - b for a, b in zip(wielomian_1, wielomian_2)]
    return wynik

def pomnoz(wielomian_1, wielomian_2):
    dlugosc = len(wielomian_1) + len(wielomian_2) - 1
    wynik = [0] * dlugosc

    for i, a in enumerate(wielomian_1):
        for j, b in enumerate(wielomian_2):
            wynik[i + j] += a * b
    return wynik

wielomian_1 = [2, -3, 0, 4]
wielomian_2 = [1, 5, 2]

print("Dodawanie:", dodaj(wielomian_1, wielomian_2))
print("Odejmowanie:", odejmij(wielomian_1, wielomian_2))
print("Mnożenie:", pomnoz(wielomian_1, wielomian_2))