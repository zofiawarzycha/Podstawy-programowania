'''
Korzystając z programu z zad 1 do wprowadzenia liczb, znaleźć wszystkie pary liczb, których w suma
daje liczbę podaną przez użytkownika.

Przykład:
Ile chcesz wprowadzić liczb? 5
Podaj liczbę: 3
Podaj liczbę: 4
Podaj liczbę: 0
Podaj liczbę: 7
Podaj liczbę: 1
Lista: [3, 4, 0, 7, 1]
Wprowadź szukaną sumę: 7
3 + 4 = 7
0 + 7 = 7
'''
def listy():
    try:
        ilosc_liczb = int(input("Ile chcesz wprowadzić liczb?\n"))

        lista_liczb = []

        for i in range(ilosc_liczb):
            liczba = int(input(f"Podaj liczbę {ilosc_liczb}:\n"))
            lista_liczb.append(liczba)

        print(f"Lista: {lista_liczb}")

        szukana_suma = int(input("Wprowadź szukaną sumę: "))

        print(f"Pary liczb, których suma wynosi {szukana_suma}:")
        znalezione_pary = False
        for i in range(len(lista_liczb)):
            for j in range(i + 1, len(lista_liczb)):
                if lista_liczb[i] + lista_liczb[j] == szukana_suma:
                    print(f"{lista_liczb[i]} + {lista_liczb[j]} = {szukana_suma}")
                    znalezione_pary = True

        if not znalezione_pary:
            print("Nie znaleziono żadnych par liczb o podanej sumie.")
    except ValueError:
        print("Podano niepoprawną wartość. Spróbuj ponownie, podając liczbę całkowitą.")


if __name__ == "__main__":
    listy()