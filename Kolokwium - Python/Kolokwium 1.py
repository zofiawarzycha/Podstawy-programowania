import math
def pobierz_promien_w_mm(lista_promieni):
    while True:
        try:
            dane = input("Podaj promień lub wpisz 'koniec': ")
            if dane.lower().strip() == "koniec":
                if len(lista_promieni) == 0:
                    print("Błąd: 'koniec' nie może być pierwszą wprowadzoną wartością.")
                    continue
                else:
                    break
            promien = float(dane)
            if promien > 0:
              lista_promieni.append(promien)
            else:
                print("Ujemna wartość promienia. Wprowadź dodatnią.")
        except ValueError:
            print("Nieprawidłowe dane. Wprowadź liczbę lub 'koniec': ")
    return lista_promieni

def max_pole_kola(prom):
    if not prom:
        return None
    max_promien = max(prom)
    return math.pi * (max_promien ** 2)

if __name__ == '__main__':
    promienie = pobierz_promien_w_mm([])
    pole = max_pole_kola(promienie)

    if pole is not None:
        print(f'Pole koła o największym promieniu wynosi: {round(pole, 2)} mm².')
    else:
        print("Brak promieni do obliczenia pola.")
