'''Napisać program proszący użytkownika o ilość liczb, które chce wprowadzić, następnie po kolei, każdą
liczbę należy wprowadzić do listy i wypisać cała zawartość listy. W przypadku podania niepoprawnej
wartości w pierwszym pytaniu program powinien powiadomić użytkownika o błędzie.

[!TIP]
Przykład:
Ile chcesz wprowadzić liczb? 3
Podaj liczbę: 12
Podaj liczbę: 33
Podaj liczbę: 2
Lista: [12, 33, 2]'''

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

def format_list(liczby):
    sformatowana_lista = []
    for liczba in liczby:
        if liczba.is_integer():
            sformatowana_lista.append(int(liczba))
        else:
            sformatowana_lista.append(liczba)
    return sformatowana_lista

wprowadz_liczby_do_listy()