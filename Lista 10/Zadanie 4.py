'''
Napisać program, który będzie obliczał silnię podanej liczby za pomocą funkcji. Następnie wykorzystać
funkcję obliczającą silnię do znalezienia silni dla liczby wybranej przez użytkownika.
'''
def silnia(n):
    if n == 0 or n == 1:
        return 1
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

liczba = int(input("Podaj liczbę, dla której chcesz obliczyć silnię: "))

wynik_silni = silnia(liczba)

print(f"Silnia liczby {liczba} wynosi {wynik_silni}.")