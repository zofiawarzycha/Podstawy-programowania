'''
Napisać funkcję która zapyta użytkownika o dodatnia liczbę całkowitą i sprawdzi przez
jakie liczby jest podzielna i wyświetli te liczby. Zastosować obsługę wyjątku w przypadku
gdy użytkownik wprowadzi cos innego niż liczbę.
'''
def czy_podzielna(liczba):
    dzielniki = []
    for i in range(1, liczba + 1):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki

def podaj_liczbe():
    while True:
        try:
            liczba = int(input("Podaj dodatnią liczbę całkowitą: "))
            if liczba > 0:
                return liczba
            else:
                print("Proszę podać liczbę większą od zera.")
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź dodatnią liczbę całkowitą.")

def main():
    liczba = podaj_liczbe()
    dzielniki = czy_podzielna(liczba)
    print(f"Liczba {liczba} jest podzielna przez: {' '.join(map(str, dzielniki))}")

if __name__ == ("__main__"):
    main()

