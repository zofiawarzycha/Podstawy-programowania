'''Korzystając z programu z zad 1 do wprowadzenia liczb, zsumować wszystkie liczby w liście i wypisać na ekran.

[!TIP]
Przykład:
Ile chcesz wprowadzić liczb? 3
Podaj liczbę: 2
Podaj liczbę: 3
Podaj liczbę: 5
Lista: [2, 3, 5]
Suma liczb: 10
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

    print("Lista: ", format_list(liczby))
    print("Suma: ", sum(format_list(liczby)))

def format_list(liczby):
    sformatowana_lista = []
    for liczba in liczby:
        if liczba.is_integer():
            sformatowana_lista.append(int(liczba))
        else:
            sformatowana_lista.append(liczba)
    return sformatowana_lista

wprowadz_liczby_do_listy()