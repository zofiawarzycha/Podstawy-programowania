'''Napisać program, który składa się z klasy reprezentującej książkę oraz funkcji, która będzie dodawała
książki do listy i wypisywała książki, które znajdują się na tej liście. Każda książka powinna mieć tytuł,
autora oraz rok wydania.'''

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def __str__(self):
        return f"'{self.tytul}' - {self.autor} ({self.rok_wydania})"

def dodaj_ksiazke(lista_ksiazek, tytul, autor, rok_wydania):
    ksiazka = Ksiazka(tytul, autor, rok_wydania)
    lista_ksiazek.append(ksiazka)
    return lista_ksiazek

def wypisz_ksiazki(lista_ksiazek):
    if not lista_ksiazek:
        print("Lista książek jest pusta.")
    else:
        print("Lista książek:")
        for ksiazka in lista_ksiazek:
            print(ksiazka)

lista_ksiazek = []
lista_ksiazek = dodaj_ksiazke(lista_ksiazek, "Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997)
lista_ksiazek = dodaj_ksiazke(lista_ksiazek, "Władca Pierścieni: Drużyna Pierścienia", "J.R.R. Tolkien", 1954)
wypisz_ksiazki(lista_ksiazek)