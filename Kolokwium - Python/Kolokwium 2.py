import math
def pobierz_wsp_punktow(list_p):
    while True:
        try:
            dane = input("Podaj współrzędne punktów: x1 x2 y1 y2 (oddzielone spacjami) lub wpisz 'koniec'.")
            if dane.lower().strip() == "koniec":
                break
            x1, x2, y1, y2 = map(float, dane.split())
            list_p.append([x1, y1, x2, y2])
        except ValueError:
            print("Niepoprawne dane.")
    return list_p

def max_odleglosc_punktow(punkty):
    max_odleglosc = 0
    for p in punkty:
        odleglosc = math.sqrt((p[2] - p[0]) ** 2 + (p[3] - p[1]) ** 2)
        if odleglosc > max_odleglosc:
            max_odleglosc = odleglosc
    return max_odleglosc

if __name__ == '__main__':
    war_punktow = [[1.1, 2.2, 3.3, 4.4], [5, 6.5, 7, 8]]

    max_odleglosc = max_odleglosc_punktow(war_punktow)

    # Wyświetlamy listę punktów
    print(f'Lista punktów: {war_punktow}')
    # Wyświetlamy odległość między punktami
    print(
        f'Największa odległość między punktami to: {round(max_odleglosc, 2)}'
    )
