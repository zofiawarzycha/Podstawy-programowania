'''Napisać funkcję, która obsługuje otwieranie pliku do wczytywania danych. Zapytać użytkownika o
nazwę pliku, który chce otworzyć do wczytania. Jeśli plik nie istnieje wypisać mu odpowiedni
komunikat. Jeśli plik istnieje wczytaj całą jego zawartość i zwróć jako wynik funkcji. Skorzystać z wiedzy
dotyczącej obsługi wyjątków.'''

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as file:
            zawartosc = file.read()
            print("Zawartość pliku wczytana pomyślnie.")
            return zawartosc
    except:
        print("Plik nie istnieje. Upewnij się, że podałeś poprawną nazwę pliku.")
        return None

if __name__ == "__main__":
    nazwa_pliku = input("Podaj nazwę pliku do wczytania: ")
    zawartosc = wczytaj_plik(nazwa_pliku)
    if zawartosc:
        print(f"Zawartość pliku: {zawartosc_pliku}")