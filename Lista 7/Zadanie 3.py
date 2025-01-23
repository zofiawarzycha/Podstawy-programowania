'''
Napisać program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. Promień
nie może być ujemny. W przypadku podania liczby ujemnej, program powinien wypisywać komunikat
informujący o błędnej wartości i nic nie liczyć.
'''
import math

r = float(input("Podaj promień koła (r): "))

def oblicz_pole_kola(r):
    return math.pi * r ** 2

def oblicz_obwod_kola(r):
    return 2 * math.pi * r

if r < 0:
    print("Błędna wartość, nie można wykonać obliczeń (promień nie może być ujemny)!")
else:
    pole = oblicz_pole_kola(r)
    obwod = oblicz_obwod_kola(r)
    print(f"Pole koła wynosi: {pole: .2f}")
    print(f"Obwód koła wynosi: {obwod: .2f}")