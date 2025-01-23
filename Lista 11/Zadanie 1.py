'''Napisać program, który korzystając z biblioteki random wybierze losowy element z listy korzystając z
funkcji choice. Lista ma być podana bezpośrednio w kodzie i powinna zawierać co najmniej 10
elementów. Następnie, utworzyć nową listę, która będzie zawierać 3 losowo wybrane elementy z
wskazanej listy, z powtórzeniami, przy użyciu metody choices z biblioteki random.
'''
import random

lista_elementow = ['gruszka', 'winogrono', 'jabłko', 'banan', 'truskawka', 'pomarańcza', 'papaja', 'kiwi', 'brzoskwinia', 'arbuz']

print(f"Losowy element z listy: {random.choice(lista_elementow)}")
print(f"Lista z trzema losowo wybranymi elementami: {random.choices(lista_elementow, k=3)}")
