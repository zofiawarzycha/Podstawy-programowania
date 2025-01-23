'''
Napisać program, który składa się z funkcji przyjmującej jako argumenty dwie liczby
całkowite x i y, następnie oblicza sumę wszystkich liczb nieparzystych znajdujących się
w przedziale od x do y (włącznie).  Program powinien pobierać argumenty x i y od
użytkownika w celu zabezpieczenia przed wprowadzeniem niepoprawnych danych,
wykorzystać obsługę wyjątków. Program powinien na koniec wyświetlać wynik.
'''
def suma_nieparzystych(x, y):
    suma = 0
    for liczba in range(x, y + 1):
        if liczba % 2 != 0:
            suma += liczba
    return suma

def glowna_funkcja():
    try:
        x = int(input("Podaj pierwszą liczbę (x) z przedziału [x, y]: "))
        y = int(input("Podaj drugą liczbę (y) z przedziału [x, y]: "))

        wynik = suma_nieparzystych(x, y)
        print(f"Suma liczb nieparzystych w przedziale od {x} do {y} wynosi {wynik}.")

    except ValueError:
        print("Wprowadziłeś niepoprawne dane. Proszę podać liczby całkowite.")

if __name__ == "__main__":
    glowna_funkcja()

