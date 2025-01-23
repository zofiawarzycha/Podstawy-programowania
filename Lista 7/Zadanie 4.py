'''
Napisać program proszący użytkownika o podanie dwóch liczb a i b. Następnie należy wyświetlić, która
z tych liczb jest większa, bądź komunikat, że są sobie równe.
'''
import math

a = float(input("Podaj pierwszą liczbę (a): "))
b = float(input("Podaj drugą liczbę (b): "))

if a > b:
    print("Pierwsza liczba (a) jest większa.")
elif a < b:
    print("Druga liczba (b) jest większa.")
else:
    print("Obie liczby są równe.")
