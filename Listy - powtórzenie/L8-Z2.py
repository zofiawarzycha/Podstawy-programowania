'''
Napisać program wyświetlający liczby całkowite z przedziału <0,y> (liczbę całkowitą y podaje
użytkownik).
'''
def wyswietl_calkowite():
    while True:
        try:
            y = int(input("Podaj liczbę całkowitą 'y' dla przedziału [0, y]: "))
            break
        except ValueError:
            print("Wartość nieprawidłowa. Podaj liczbę całkowitą.")
    if y >= 0:
        print(f"Liczby całkowite z przedziału [0, {y}] to: ")
        for i in range(0, y + 1):
            print(i)
    else:
        print("Liczba musi być większa lub równa 0.")

wyswietl_calkowite()