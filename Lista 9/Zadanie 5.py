'''
Przygotować słownik zawierający min 5 kierunków studiów oferowanych na Politechnice Wrocławskiej
razem z wydziałem, na którym są oferowane. Następnie napisać program, który będzie wskazywał na
jakim wydziale znajduje się kierunek wyszukiwany przez użytkownika. W przypadku braku takiego
kierunku poinformuj użytkownika, że nie może studiować tego kierunku na Politechnice Wrocławskiej.

Przykład:
Podaj nazwę kierunku studiów: Informatyka
Kierunek Informatyka znajduje się na Wydział Elektroniki.

Przykład:
Podaj nazwę kierunku studiów: Garncarstwo
Nie możesz studiować kierunku Garncarstwo na Politechnice Wrocławskiej.
'''
def kierunki():
    kierunki_studiow = {
        "Informatyka": "Wydział Informatyki i Telekomunikacji",
        "Automatyka i Robotyka": "Wydział Mechaniczny",
        "Budownictwo": "Wydział Budownictwa Lądowego i Wodnego",
        "Architektura": "Wydział Architektury",
        "Elektronika": "Wydział Elektroniki, Fotoniki i Mikrosystemów"
    }

    kierunek = input("Podaj kierunek studiów, aby sprawdzić na jakim jest wydziale: ")

    if kierunek in kierunki_studiow:
        wydzial = kierunki_studiow[kierunek]
        print(f"Kierunek '{kierunek}' znajduje się na: {wydzial}.")
    else:
        print(f"Nie możesz studiować kierunku '{kierunek}' na Politechnice Wrocławskiej.")

if __name__ == "__main__":
    kierunki()