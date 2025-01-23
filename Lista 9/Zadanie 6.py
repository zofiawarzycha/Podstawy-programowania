'''
Napisać program, który pobierze od użytkownika zdanie, a następnie policzy występowania
poszczególnych znaków w danym zdaniu (oprócz znaku spacji), umieści wynik w słowniku i wypisze go
na ekran. Zastosować metodę .lower(), aby do słownika wprowadzać tylko małe litery niezależnie od
tego jak zostały wprowadzone przez użytkownika. Litery mają być kluczem, wartością liczba wystąpień.

Przykład:
Podaj zdanie: Python jest SUPER!
{'p': 2, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'j': 1, 'e': 2, 's': 2, 'u': 1, 'r': 1, '!': 1}
'''

def liczenie():
    zdanie = input("Podaj zdanie: ")

    licznik_znakow = {}

    for znak in zdanie.lower():
        if znak != " ":
            if znak in licznik_znakow:
                licznik_znakow[znak] += 1
            else:
                licznik_znakow[znak] = 1

    print("Występowania poszczególnych znaków w zdaniu:")
    for znak, liczba in licznik_znakow.items():
        print(f"'{znak}': {liczba}")

if __name__ == "__main__":
    liczenie()