'''
Napisać program, który narysuje z gwiazdek (*) kwadrat 10 na 10.
'''
def narysuj_kwadrat():
    for i in range(10):
        for j in range(10):
            print("*", end=' ')
        print()

narysuj_kwadrat()