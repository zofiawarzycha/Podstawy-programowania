'''
Napisać program, który dla wprowadzonego przez użytkownika ciągu liczb rzeczywistych wyznacza ich
średnią arytmetyczną. Wprowadzanie ciągu kończy się poprzez wprowadzenie napisu ’end’. Program
powinien raportować błąd, jeśli ’end’ jest pierwszą podaną wartością. Przykładowo, dla wejścia:
1
-22
8
-3.5
13
end
Poprawną odpowiedzią jest -0.7.
'''
def oblicz_srednia():
    liczby = []

    while True:
        wejscie = input("Podaj liczby rzeczywiste (lub 'end', aby zakończyć): ")
        if wejscie.lower().strip() == "end":
            if len(liczby) == 0:
                print("Błąd: 'end' nie może być pierwszą wprowadzoną wartością.")
                continue
            else:
                break
        try:
            liczba = float(wejscie)
            liczby.append(liczba)
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę rzeczywistą lub 'end'.")
    if len(liczby) > 0:
        srednia = sum(liczby) / len(liczby)
        print(f"Średnia arytmetyczna wprowadzonych liczb wynosi {srednia}.")

oblicz_srednia()


