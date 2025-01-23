'''Napisać program, który polega na zliczaniu unikalnych słów w pliku tekstowym i zapisaniu ich wraz z
liczbą wystąpień do innego pliku.
'''
def licz_unikalne_slowa(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego):
    try:
        with open(nazwa_pliku_wejsciowego, 'r') as plik_wejsciowy:
            tekst = plik_wejsciowy.read()
            slowa = tekst.split()
            zliczenia = {}

            for slowo in slowa:
                if slowo in zliczenia:
                    zliczenia[slowo] += 1
                else:
                    zliczenia[slowo] = 1

            with open(nazwa_pliku_wyjsciowego, 'w') as plik_wyjsciowy:
                for slowo, wystapienia in zliczenia.items():
                    plik_wyjsciowy.write(f"Słowo '{slowo} wystąpiło {wystapienia} razy.\n")

        print(f"Zliczono unikalne słowa z pliku '{nazwa_pliku_wejsciowego}' i zapisano do '{nazwa_pliku_wyjsciowego}'.")

    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku_wejsciowego}' nie istnieje.")