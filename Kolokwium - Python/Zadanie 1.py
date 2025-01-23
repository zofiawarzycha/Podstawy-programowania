'''Napisać program który składa się z funkcji przyjmującej jedna liczbę
naturalna n jako argument i oblicza pierwszych n kolejnych potęg liczby 2,
ale tylko te które są parzyste. Program powinien następnie wyświetlić wynik.
Zastosować obsługę wyjątku w przypadku gdy użytkownik wprowadzi cos innego
niż liczbę naturalna.'''

def oblicz_parzyste_potegi(n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("Liczba musi być dodatnia i większa od zera.")

        potegi = [2**i for i in range(1, n+1) if (2**i) % 2 == 0]
        return potegi

    except ValueError as blad:
        return f"Błąd: {blad}. Upewnij się, że wprowadzona liczba jest dodatnią liczbą naturalną."

if __name__ == "__main__":
    n = input("Podaj liczbę naturalną: ")
    wynik = oblicz_parzyste_potegi(n)
    print("Wynik:", wynik)
