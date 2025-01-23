'''
najpierw musimy zaimportować moduł "datetime", który pomaga pracować z datami i czasem
- podaje aktualną datę, nie musimy tego robić ręcznie (automatyzacja)
- jest też pewność że ta data jest zawsze aktualna (dokładność)
- dostarcza gotowe funkcje i metody
'''

import datetime
#ustawiamy aktualny rok
current_year = datetime.datetime.now().year
#musimy poprosić użytkownika o podanie jego imienia (funkcja input)
name = input("Podaj swoje imię:\n")
#musimy uzyskać rok urodzenia użytkownika i przekonwertować go ze stringa na integer
birth_year = int(input("Podaj swój rok urodzenia:\n"))
#obliczamy wiek użytkownika
age = current_year - birth_year
#teraz musimy wypluć całą funkcję
#używamy prefixa f, żeby dać znać że ciąg znaków jest formatowany
#za pomocą nawiasów klamrowych aby wskazać miejsce gdzie chcemy wstawić wartości zmiennych
print(f"{name}, masz {age} lat.")
