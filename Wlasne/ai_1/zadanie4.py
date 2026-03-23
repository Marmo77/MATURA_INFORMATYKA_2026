# x, y = l.c. -10000 <= x,y, <= 10000
import math

# 4.1.
# trzeba podać ile leży w pierwszej ćwiartce układu wspolrzednych
# czyli x > 0 i y > 0

# trzeba podać "kordynaty" tego który jest najdalej od punktu (0,0) czyli odleglosc wzgledem punku pierwiastek z ( Vx^2+y^2 )
# czyli jesli x,y = 3,4 => 3^2+4^2 => 25 pierwiastek z tego => 5, czyli oddalony jest o 5


def licz_odleglosc(x: int,y: int):
    #liczy odległość miedzy punktem (0,0) a (x,y)

    kwadrat = x**2 + y**2
    wynik = math.sqrt(kwadrat)
    return wynik

najdalszy = 0
najdalszy_x, najdalszy_y = 0, 0
liczba_punktow_pierwszej_cwiarki = 0
with open("punkty.txt", "r") as plik:
    for line in plik:
        line = line.strip()
        x,y = line.split(" ")
        x,y = int(x),int(y)
        # print(f"{x},{y}")

        if x > 0 and y > 0: # jest w pierwszej cwiarce
            liczba_punktow_pierwszej_cwiarki += 1
            odleglosc = licz_odleglosc(int(x),int(y))
            # print(f"Odległość od punktu 0: {odleglosc}")
            if odleglosc > najdalszy:
                najdalszy = odleglosc
                najdalszy_x = x
                najdalszy_y = y
print(f"Liczba punktów w I ćwiartce: {liczba_punktow_pierwszej_cwiarki}")
print(f"Najdalszy punkt: {najdalszy_x}, {najdalszy_y}")

# ============================
# ZADANIE 4.2.

print("--------")

#punkty symetryczne, czyli jeśli x,y są takie same lub odwrotne czyli jeśli x=y albo x=-y
# np. dla x,y= (3,3) => 3=3, x,y =(-3,3) => x != y, ale za to -3 = -3

symetryczne = 0
kordynaty = []
with open("punkty.txt", "r") as plik:
    for line in plik:
        line = line.strip()
        x,y = line.split(" ")
        x,y = int(x),int(y)

        if x == y or x == (y * -1): # jest symetryczna
            # print(f"Symetryczne: {x}, {y}")
            symetryczne += 1

        # sprawdzanie czy istnieje para z odbiciem osi OX (czyli x jest taki sam ale y jest odwrotny
        # będzie poza plikiem --> dodamy kordynaty do tablicy
        kordynaty.append([x,y])

# print(kordynaty)

pierwsza_para_lustrzana = ""
szukaj = 1
#dla kazdego elementu sprawdzamy następne czy x jest taki sam, jeśli jest to sprawdzamy czy X jest odwrotny
for idx, kordynaty_xy in enumerate(kordynaty):
    x,y = kordynaty_xy

    for j in range(idx, len(kordynaty)):
        # od idx czyli zalozmy ze jest 5 elementow w liscie
        # to pierwszy jest sprawdzany od idx: 0 do 5, a trzeci element w liscie
        # jest sprawdzany od idx: 2 do 5 bo poprzednie i tak sprawdzone zostały wczesniej
        # print(f"Dla: {x} i {y}")
        szukane_x,szukane_y = kordynaty[j]
        # print(szukane_x, szukane_y)
        if szukane_x == x and szukaj == 1:
            if y == (-1*szukane_y) and y != 0:
                pierwsza_para_lustrzana = f"Para lustrzana: {x,y} oraz {szukane_x,szukane_y}"
                szukaj = 0

if pierwsza_para_lustrzana == "":
    pierwsza_para_lustrzana = "NIE"
print(f"Symetryczne: {symetryczne}")
print(pierwsza_para_lustrzana)


#===========================
# Zadanie 4.3.
print("----------")

#pitagoras przyklad. Kiedy kąt prosty kiedy a^2 + b^2 = c^2, 2 krotsze boki do ^2 = najdluzszy bok do ^2
#wtedy jest kat prosty

#przyklad
#dl1 = 4
#dl2 = 3
#dl3 = 5
#pitagoras: 4^2 + 3^2 = 5^2 => 16 + 9 = 25 => 25 |:V => 5 = dl3
#wtedy jest kąt prosty

# tylko 3 elementy od czyli 1,2,3 pozniej 3,4,5 czyli:
# szukamy elementów z granicy (od 0 do dlugosc tablicy -2 czyli ostatni element będzie
# np. 6,7,8 i nie wyjdzie za tablice, bo jesli bylby 7,8,NaN to bysmy wyszli za pętle

def liczenie_prostej(x1,y1,x2,y2):
    # definicja dlugosci prostej:
    # Pierwiastek z: (x1-x2)^2 + (y1-y2)^2
    pierwiastkowana = (x1-x2)**2 + (y1-y2)**2
    # dlugosc_prostej = math.sqrt(pierwiastkowana)
    return pierwiastkowana

wszystkie_kordynaty = []
ile_jest_prostokatnych = 0
with open("punkty.txt", "r") as plik:
    for linia in plik:
        linia = linia.strip()
        x,y = linia.split(" ")
        x,y = int(x),int(y)
        wszystkie_kordynaty.append([x,y])


# print(wszystkie_kordynaty)
for idx in range(len(wszystkie_kordynaty)-2):
    kordynaty_1 = wszystkie_kordynaty[idx]
    kordynaty_2 = wszystkie_kordynaty[idx+1]
    kordynaty_3 = wszystkie_kordynaty[idx+2]

    k1_x,k1_y = kordynaty_1[0],kordynaty_1[1]
    k2_x,k2_y = kordynaty_2[0],kordynaty_2[1]
    k3_x,k3_y = kordynaty_3[0],kordynaty_3[1]

    # print(f"Kordynaty 1: {kordynaty_1}")
    # print(f"Kordynaty 2: {kordynaty_2}")
    # print(f"Kordynaty 3: {kordynaty_3}")

    # potrzebujemy obliczyć 3 proste: |AB| |AC| |BC|, załóżmy że k1 = A, k2=B, k3=C
    #teraz liczymy długości prostych
    prosta_AB = liczenie_prostej(k1_x,k1_y,k2_x,k2_y)
    prosta_AC = liczenie_prostej(k1_x,k1_y,k3_x,k3_y)
    prosta_BC = liczenie_prostej(k2_x,k2_y,k3_x,k3_y)

    proste = [prosta_AB,prosta_AC,prosta_BC]
    proste.sort()

    if proste[0] + proste[1] == proste[2]:
        ile_jest_prostokatnych += 1
        # print("jest prostokątny")
        # print(f"{proste[0]+proste[1]} = {proste[2]}")

print(f"Trójkątów Prostokątnych jest: {ile_jest_prostokatnych}")
