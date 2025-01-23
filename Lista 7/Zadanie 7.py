'''
Napisać program, który sprawdzi czy z podanych długości można stworzyć trójkąt i wypisze odpowiedni
komunikat.
'''

a = float(input("Podaj pierwszą liczbę (długość boku 'a' trójkąta): "))

b = float(input("Podaj drugą liczbę (długość boku 'b' trójkąta): "))

c = float(input("Podaj trzecią liczbę (długość boku 'c' trójkąta): "))

if a + b > c and b + c > a and a + c > b:
    print("Z podanych długości można stworzyć trójkąt.")
else:
    print('''Z podanych długości NIE można stworzyć trójkąta.
Suma długości dwóch boków trójkąta musi być większa od długości trzeciego boku.
          ''')