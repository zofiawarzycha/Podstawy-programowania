'''
Napisać program który będzie pobierał od użytkownika liczby całkowite
i dodawał je do listy dopóki użytkownik nie wpisze liczby 0. Po jej
wpisaniu przerywa się możliwość wpisywania kolejnych liczb. Każda z liczb
należy dopisać do listy. Następnie na istniejącej liście dokonać operacji
sumowania wszystkich liczb w niej umieszczonych, wyświetlić sumę oraz
wyświetlić zawartość tej listy (nie cala listę). Zastosować obsługę wyjątku
w przypadku, gdy użytkownik wprowadzi cos innego niż liczbę całkowita.
'''

def zbieranie_liczb():
    liczby = []

    while True:
        try:
            liczba = int(input("Podaj liczbę całkowitą: "))
            if liczba == 0:
                break
            liczby.append(liczba)
        except ValueError:
            print("Wprowadziłeś niepoprawną wartość. Proszę podać liczbę całkowitą.")

    suma = sum(liczby)

    print("Suma liczb:", suma)
    print("Zawartość listy:", ' '.join(map(str, liczby)))

if __name__ == "__main__":
        zbieranie_liczb()


