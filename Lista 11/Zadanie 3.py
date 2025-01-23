'''Napisać kod, który sprawdzi, jak często słowo "kot" występuje w pliku "tekst.txt".
Przykład:
Jeśli w pliku "tekst.txt" znajduje się tekst "Kot jest bardzo fajnym zwierzęciem", to kod powinien
wyświetlić "Słowo 'kot' wystąpiło 1 razy w pliku 'tekst.txt'."
Użyć metody count do zliczenia wystąpienia słowa w całym pliku. Uwzględnić wielkość liter dla
szukanych stringów.
'''

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            return plik.read()
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")
    except Exception as blad:
        print(f"Wystąpił błąd: {blad}")
        return None

def zlicz_wystapienia_slowa(tekst, slowo):
    slowo = slowo.lower()
    return tekst.lower().split().count(slowo)

if __name__ == "__main__":
    nazwa_pliku = "tekst.txt"
    slowo_do_zliczenia = "kot"
    zawartosc_pliku = wczytaj_plik(nazwa_pliku)

    if zawartosc_pliku:
        liczba_wystapien = zlicz_wystapienia_slowa(zawartosc_pliku, slowa_do_zliczenia)
        print(f"Słowo '{slowo_do_zliczenia} wystąpiło {liczba_wystapien} razy w pliku '{nazwa_pliku}'.")
