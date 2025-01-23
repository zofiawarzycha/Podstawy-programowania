'''
Napisać program sprawdzający czy osoba urodzona w danym roku jest pełnoletnia
'''

import datetime

current_year = datetime.datetime.now().year

name = input("Podaj swoje imię:\n")
birth_year = int(input("Podaj swój rok urodzenia:\n"))

age = current_year - birth_year

if age >= 18:
    print(f"{name}, masz {age} lat, jesteś pełnoletni/a.")
else:
    print(f"{name}, masz {age} lat, jesteś niepełnoletni/a.")