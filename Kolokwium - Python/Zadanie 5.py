'''
Napisać funkcje, która przyjmuje listę wartości temperatury wyrażonych w stopniach
Celsjusza i zwraca listę odpowiadających im temperatur w kelwinach. Lista temperatur
w stopniach Celsjusza powinna zostać podana przez użytkownika i zawierać 5
temperatur. Wynikiem funkcji ma być lista temperatur w kelwinach. Zastosować obsługę
wyjątku w przypadku gdy użytkownik wprowadzi cos innego niż liczbę.
'''

def celsius_to_kelvin(celsius_temps):
    kelvin_temps = []
    for temp in celsius_temps:
        kelvin_temps.append(temp + 273.15)
    return kelvin_temps

def pobierz_temperatury():
    celsius_temps = []
    while len(celsius_temps) < 5:
        try:
            temp = float(input("Podaj temperaturę w stopniach Celsiusza: "))
            celsius_temps.append(temp)
        except ValueError:
            print("Wprowadziłeś niepoprawną wartość. Proszę podać liczbę.")
    return celsius_temps

def main():
    celsius_temps = pobierz_temperatury()
    kelvin_temps = celsius_to_kelvin(celsius_temps)
    print("Temperatury w Kelwinach:", kelvin_temps)

if __name__ == "__main__":
    main()
