'''Napisać program, który będzie zawierał funkcje do analizy danych. Funkcje, jakie powinny zostać
zaimplementowane: srednia_wydajnosc, maksymalna_wydajnosc, minimalna_wydajnosc,
odchylenie_standardowe. Wydajności, które należy zastosować:
wydajności = [120, 150, 130, 170, 140].
a) Rozwiązać zadanie bez korzystania z wbudowanych funkcji.
b) Rozwiązać zadanie z wbudowanymi funkcjami.
Wyniki wyświetlić na ekranie komputera
'''
# a)
def srednia_wydajnosc(wydajnosci):
    suma = 0
    for wydajnosc in wydajnosci:
        suma += wydajnosc
    return suma/len(wydajnosci)

def maksymalna_wydajnosc(wydajnosci):
    max_wydajnosc = wydajnosci[0]
    for wydajnosc in wydajnosci:
        if wydajnosc > max_wydajnosc:
            max_wydajnosc = wydajnosc
    return max_wydajnosc

def minimalna_wydajnosc(wydajnosci):
    min_wydajnosc = wydajnosci[0]
    for wydajnosc in wydajnosci:
        if wydajnosc > min_wydajnosc:
            min_wydajnosc = wydajnosc
    return min_wydajnosc

def odchylenie_standardowe(wydajnosci):
    srednia = srednia_wydajnosc(wydajnosci)
    suma_kwadratow = 0
    for wydajnosc in wydajnosci:
        suma_kwadratow += (wydajnosc - srednia) ** 2
    wariancja = suma_kwadratow / len(wydajnosci)
    return wariancja ** 0.5

wydajnosci = [120, 150, 130, 170, 140]

print("Średnia wydajność:", srednia_wydajnosc(wydajnosci))
print("Maksymalna wydajność:", maksymalna_wydajnosc(wydajnosci))
print("Minimalna wydajność:", minimalna_wydajnosc(wydajnosci))
print("Odchylenie standardowe:", odchylenie_standardowe(wydajnosci))

# b)
import statistics

wydajnosci = [120, 150, 130, 170, 140]

def srednia_wydajnosc(wydajnosci):
    return statistics.mean(wydajnosci)

def maksymalna_wydajnosc(wydajnosci):
    return max(wydajnosci)

def minimalna_wydajnosc(wydajnosci):
    return min(wydajnosci)

def odchylenie_standardowe(wydajnosci):
    return statistics.stdev(wydajnosci)

print("Średnia wydajność:", srednia_wydajnosc(wydajnosci))
print("Maksymalna wydajność:", maksymalna_wydajnosc(wydajnosci))
print("Minimalna wydajność:", minimalna_wydajnosc(wydajnosci))
print("Odchylenie standardowe:", odchylenie_standardowe(wydajnosci))
