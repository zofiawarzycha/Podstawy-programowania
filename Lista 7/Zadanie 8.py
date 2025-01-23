'''
Napisać program, który pobierze od studenta liczbę punktów i oceni go według podanej skali. Ponadto
użytkownik może wybrać w jakiej formie chce dostać ocenę (liczbowo lub słownie lub oba)
Skala:
<0; 50) 2.0 (niedostateczny)
<50;60) 3.0 (dostateczny)
<60;70) 3.5 (dostateczny plus)
<70;80) 4.0 (dobry)
<80;90) 4.5 (dobry plus)
<90;100) 5.0 (bardzo dobry)
<100> 5.5 (celujący)
'''
pkt = float(input("Podaj liczbę punktów: "))
forma_oceny = input("W jakiej formie chcesz otrzymać ocenę? (liczbowo/słownie/oba): ").strip().lower()

def ocena_liczbowo(pkt):
    if pkt < 50:
        return 2.0
    elif pkt < 60:
        return 3.0
    elif pkt < 70:
        return 3.5
    elif pkt < 80:
        return 4.0
    elif pkt < 90:
        return 4.5
    elif pkt < 100:
        return 5.0
    else:
        return 5.5

def ocena_slownie(pkt):
    if pkt < 50:
        return "niedostateczny"
    elif pkt < 60:
        return "dostateczny"
    elif pkt < 70:
        return "dostateczny plus"
    elif pkt < 80:
        return "dobry"
    elif pkt < 90:
        return "dobry plus"
    elif pkt < 100:
        return "bardzo dobry"
    else:
        return "bardzo dobry plus"

if forma_oceny == "liczbowo":
    print(f"Twoja ocena to {ocena_liczbowo(pkt)}")
elif forma_oceny == "słownie":
    print(f"Twoja ocena to {ocena_slownie(pkt)}")
elif forma_oceny == "oba":
    print(f"Twoja ocena to {ocena_liczbowo(pkt)} - {ocena_slownie(pkt)}")
else:
    print("Nieprawidłowa forma oceny. Wybiesz: liczbowo/słownie/oba.")