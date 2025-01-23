'''
Napisać program, który wyświetli wszystkie liczby z przedziału od 50 do 100 podzielne przez dowolną
liczbę k, którą podaje użytkownik.
'''
def wyswietl_liczby_podzielne_przez_k():
    while True:
        try:
            k = int(input("Podaj liczbę całkowitą 'k': "))
            if k == 0:
                print("Nieprawidłowa wartość. Liczba 'k' nie może być zerem")
                continue
            break
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą.")
    print(f"Liczby z przedziału od 50 do 100, które są podzielne przez {k}, to: ")
    for i in range(50, 101):
        if i % k == 0:
            print(i)

wyswietl_liczby_podzielne_przez_k()
