'''
Napisać program wyświetlający liczby całkowite z przedziału <x,y> (liczby całkowite x i y podaje
użytkownik).
'''
def wyswietl_calkowite():
    while True:
        try:
            x = int(input("Wprowadź liczbę 'x' dla przedziału [x, y]: "))
            break
        except ValueError:
            print("Nieprawidłowa wartość. Wprowadź liczbę całkowitą.")
    while True:
        try:
            y = int(input("Wprowadź liczbę 'y' dla przedziału [x, y]: "))
            if y>x:
                break
            else:
                print(f"Liczba 'y' musi być większa od liczby '{x}'.")
        except ValueError:
            print("Nieprawidłowa wartość. Wprowadź liczbę całkowitą.")
    if y >= x:
        print(f"Liczby całkowite z przedziału [{x}, {y}] to: ")
        for i in range (x, y + 1):
            print(i)
wyswietl_calkowite()