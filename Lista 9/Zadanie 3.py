'''
Korzystając z programu z zad 1 do wprowadzenia liczb, znaleźć najmniejszą i największą wartość w
liście i wypisać ją na ekran

Przykład:
Ile chcesz wprowadzić liczb? 4
Podaj liczbę: 2
Podaj liczbę: 3
Podaj liczbę: 5
Podaj liczbę: 6
Lista: [2, 3, 5, 6]
Najmniejsza wartość: 2
Największa wartość: 6

Przykład:
Ile chcesz wprowadzić liczb? -2
Błędna wartość, wprowadź liczbę większą niż 0.
'''
def wprowadz_liczby_do_listy():
    while True:
        try:
            n = int(input("Ile chcesz wprowadzić liczb?: "))
            if n <= 0:
                print("Liczba musi być większa od zera.")
                continue
            break
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą.")

    liczby = []
    for i in range(n):
        while True:
            try:
                liczba = float(input(f"Podaj liczbę ({i + 1}/{n}): "))
                liczby.append(liczba)
                break
            except ValueError:
                print("Niepoprawna wartość. Podaj liczbę.")

    sformatowana_lista = format_list(liczby)
    print("Lista: ", sformatowana_lista)

    najmniejsza_liczba = min(sformatowana_lista)
    najwieksza_liczba = max(sformatowana_lista)
    print("Najmniejsza liczba: ", najmniejsza_liczba)
    print("Największa liczba: ", najwieksza_liczba)

def format_list(liczby):
    sformatowana_lista = []
    for liczba in liczby:
        if liczba.is_integer():
            sformatowana_lista.append(int(liczba))
        else:
            sformatowana_lista.append(liczba)
    return sformatowana_lista

wprowadz_liczby_do_listy()