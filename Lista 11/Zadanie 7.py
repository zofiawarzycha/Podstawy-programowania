'''Doklasy książka z poprzedniego zadania dopisać klasę biblioteka która będzie składać się z obiektów
klasy książka. Do przechowywania książek w klasie biblioteka użyć zwykłej listy.
Klasa biblioteka powinna posiadać następujące metody (taka funkcja należąca do klasy):
- dodaj_ksiazke() - dodaje książkę do biblioteki
- usun_ksiazke_o_tytule() - usuwa książkę o wskazanym tytule z biblioteki
- wypisz_zawartosc_biblioteki() - wypisuje wszystkie książki w bibliotece
- znajdz_ksiazke_autora() - wypisuje wszystkie książki wskazanego autora
'''
class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def __str__(self):
        return f"'{self.tytul}' - {self.autor} ({self.rok_wydania})"

class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def usun_ksiazke_o_tytule(self, tytul):
        self.ksiazki = [ksiazka for ksiazka in self.ksiazki if ksiazka.tytul != tytul]

    def wypisz_zawartosc_biblioteki(self):
        for ksiazka in self.ksiazki:
            print(ksiazka)

    def znajdz_ksiazke_autora(self, autor):
        for ksiazka in self.ksiazki:
            if ksiazka.autor == autor:
                print(ksiazka)

ksiazka1 = Ksiazka("Harry Potter", "J.K. Rowling", 1997)
ksiazka2 = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954)
biblioteka = Biblioteka()
biblioteka.dodaj_ksiazke(ksiazka1)
biblioteka.dodaj_ksiazke(ksiazka2)
biblioteka.wypisz_zawartosc_biblioteki()
biblioteka.znajdz_ksiazke_autora("J.K. Rowling")
biblioteka.usun_ksiazke_o_tytule("Harry Potter")
biblioteka.wypisz_zawartosc_biblioteki()

'''Wykonać menu które pozwoli wykorzystać powyższe klasy i daje użytkownikowi możliwość tworzenia
książek i korzystania z biblioteki. Pamiętać, że program powinien działać do czasu aż użytkownik nie
wybierze z menu opcji do zamknięcia programu. Do tego celu można wykorzystać pętlę while. 
'''

def menu():
    biblioteka = Biblioteka()

    while True:
        print('''
         --- MENU ---
        1. Dodaj książkę
        2. Usuń książkę o tytule
        3. Wypisz zawartość biblioteki
        4. Znajdź książki autora
        5. Wyjście
        ''')
        wybor = input("Wybierz opcję (1-5): ")

        if wybor == '1':
            tytul = input("Podaj tytuł książki: ")
            autor = input("Podaj autora książki: ")
            rok_wydania = input("Podaj rok wydania książki: ")
            ksiazka = Ksiazka(tytul, autor, rok_wydania)
            biblioteka.dodaj_ksiazke(ksiazka)
            print(f"Książka '{tytul}' dodana do biblioteki.")
        elif wybor == '2':
            tytul = input("Podaj tytuł ksiązki do usunięcia: ")
            biblioteka.usun_ksiazke_o_tytule(tytul)
            print(f"Książka o tytule '{tytul}' została usunięta z biblioteki.")
        elif wybor == '3':
            print("Zawartość biblioteki:")
            biblioteka.wypisz_zawartosc_biblioteki()
        elif wybor == '4':
            autor = input("Podaj autora książki: ")
            print(f"Książki autora {autor}:")
            biblioteka.znajdz_ksiazke_autora(autor)
        elif wybor == '5':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    menu()