'''
Napisać funkcję, która przyjmuje wartość temperatury w Kelvinach i zwraca wartość wyrażoną w
stopniach Celsjusza. W przypadku podania wartości ujemnej funkcja zwraca None.
'''
def kelvin_na_celsjusz():

    temp_kelvin = float(input("Podaj temperaturę w Kelvinach (większą od 0): "))

    if temp_kelvin < 0:
        return None

    temp_celsjusz = temp_kelvin - 273.15
    return temp_celsjusz

wynik = kelvin_na_celsjusz()
if wynik is not None:
    print((f"Temperatura w stopniach Celsjusza wynosi {wynik}."))
else:
    print("Podano ujemną wartość w Kelvinach, co jest niemożliwe.")

