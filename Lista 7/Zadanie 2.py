import math

a = float(input("Podaj pierwszą liczbę (a): "))
b = float(input("Podaj drugą liczbę (b): "))

suma = a + b
roznica = a - b
iloczyn = a * b

if b != 0:
    iloraz = a / b
else:
    iloraz = "Nie można dzielić przez zero!"

if (a + b) >= 0:
    pierwiastek_kwadratowy = math.sqrt(a + b)
else:
    pierwiastek_kwadratowy = "Nie można wyznaczyć pierwiastka z liczby ujemnej"

a_do_potegi_b = a ** b
b_do_potegi_a = b ** a

print("Suma a + b:", suma)
print("Różnica a - b:", roznica)
print("Iloczyn a * b:", iloczyn)
print("Iloraz a / b:", iloraz)
print("Pierwiastek kwadratowy z (a + b):", pierwiastek_kwadratowy)
print("a^b:", a_do_potegi_b)
print("b^a:", b_do_potegi_a)
