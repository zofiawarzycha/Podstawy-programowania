'''
Napisać program, który narysuje z gwiazdek (*) kwadrat 10 na 10.
'''
def narysuj_kwadrat():
    rozmiar = 10
    for i in range(rozmiar):
        for j in range(rozmiar):
            print('*', end=' ')
        print()
narysuj_kwadrat()