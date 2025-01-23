'''
Napisać program, gdzie zadaniem gracza jest odgadnięcie liczby. Liczba jest wprowadzona na stałe w
kodzie. Jeżeli użytkownik poda za dużą liczbę program wyświetli komunikat „Szukana wartość jest
mniejsza”. Jeżeli wprowadzi za małą liczbę program wyświetli „Szukana wartość jest większa”. Po
odgadnięciu liczby gracz dowiaduje się po ilu próbach udało mu się zakończyć grę.
'''
def zgadywanie_liczby():
    szukana_liczba = 19
    licznik_prob = 0

    print("Witaj w grze zgadywanka liczbowa! Odgadnij liczbę z przedziału od 1 do 100!")

    while True:
        liczba_gracza = int(input("Podaj swoją liczbę: "))
        licznik_prob += 1
        if liczba_gracza > szukana_liczba:
            print("Szukana liczba jest mniejsza.")
        elif liczba_gracza < szukana_liczba:
            print("Szukana liczba jest większa.")
        else:
            print(f"Gratulacje! Udało ci się odgadnąć liczbę ({szukana_liczba}) po tylu próbach: {licznik_prob}!")
            break

zgadywanie_liczby()