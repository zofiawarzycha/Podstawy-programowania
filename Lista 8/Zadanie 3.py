'''
Napisać program wyświetlający liczby całkowite z przedziału <x,y> (liczby całkowite x i y podaje
użytkownik).
'''
def wyswietl_liczby():
    while True:
        try:
            x = int(input("Wprowadź liczbę całkowitą 'x' dla przedziału <x,y>: "))
            break
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą.")

    while True:
        try:
            y = int(input(f"Wprowadź liczbę całkowitą 'y' dla przedziału <{x},y>: "))
            if y >= x:
                break
            else:
                print(f"Liczba 'y' musi być większa od liczby '{x}'.")
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę całkowitą, większą od 'x'.")

    if y >= x:
        print(f"Liczby całkowite z przedziału <{x}, {y}> to: ")
        for i in range(x, y + 1):
            print(i)

wyswietl_liczby()

