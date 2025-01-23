'''
Napisać program, który sprawdzi czy podana liczba jest parzysta i wyświetli odpowiedni komunikat.
'''

liczba = int(input("Podaj liczbę: "))

if liczba % 2 == 0:
    print(f"Liczba {liczba} jest parzysta.")
else:
    print(f"Liczba {liczba} jest nieparzysta.")
