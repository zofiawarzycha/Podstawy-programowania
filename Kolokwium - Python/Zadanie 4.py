'''
Napisać program który pobiera od użytkownika liczby całkowite i dodaje je do listy,
dopóki suma wprowadzanych liczb nie przekroczy wartości 100. Po osiągnieciu tej sumy
pogram powinien przerwać wprowadzanie kolejnych liczb. Każda z liczb należy dopisać
do listy. Następnie wyświetlić sumę oraz ilość wprowadzonych liczb. Nie można używać
wbudowanej funkcji sum ani len. Zastosować obsługę wyjątku w przypadku, gdy
użytkownik wprowadzi cos innego niż liczbę całkowita.
'''

def zbieranie_liczb():
    liczby = []
    suma = 0
    ilosc = 0

    while suma <= 100:
        try:
            liczba = int(input("Podaj liczbę całkowitą: "))
            liczby.append(liczba)
            suma += liczba
            ilosc += 1
            if suma > 100:
                break
        except ValueError:
            print("Wprowadziłeś niepoprawną wartość. Proszę podać liczbę całkowitą.")

    print(f"Suma liczb: {suma}.")
    print(f"Ilość wprowadzonych liczb: {ilosc}.")

if __name__ == "__main__":
    zbieranie_liczb()
