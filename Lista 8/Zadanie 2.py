'''
Napisać program wyświetlający liczby całkowite z przedziału <0,y> (liczbę całkowitą y podaje
użytkownik).
'''
def wyswietl_liczby():
    while True:
        try:
            y = int(input("Podaj liczbę całkowitą y: "))
            break
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą")

    if y >= 0:
        print(f"Liczby całkowite z przedziału <0, {y}> to: ")
        for i in range(0, y + 1):
            print(i)
    else:
        print("Liczba musi być większa lub róna 0.")

wyswietl_liczby()