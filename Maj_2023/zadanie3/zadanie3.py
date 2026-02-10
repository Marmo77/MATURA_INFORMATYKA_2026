
plik = open('pi_przyklad.txt', 'r')
# plik = open('pi.txt', 'r')

# Zadanie 3.1.

# - trzeba znaleźć wszystkie dwuszyfrowe
# - przechodzimy przez kazdy element czyli przez range dlugosci -1
wszystkie_pary = {}
for i in range(10): # i = pierwsza liczba
    # wszystkie_pary[i] = 0
    for j in range(10):
        para = str(f"{i}{j}")
        wszystkie_pary[para] = 0
# print(wszystkie_pary)
# uzupełnianie par wszyskite mozliwe kombinacje


znaki = plik.readlines()

pary: dict[str, int] = wszystkie_pary # lista wszystkich par
for i in range(len(znaki)-1):
    znaki[i], znaki[i+1] = znaki[i].strip(), znaki[i+1].strip()

    para = str(f"{znaki[i]}{znaki[i+1]}")
    if para in wszystkie_pary:
        pary[para] += 1
    else:
        pary[para] = 1

# print(pary)
powyzej90 = 0
for k, v in pary.items(): # przez kazdą pare przechodzimy
    if int(k) > 90: # jeśli klucz czyli liczba wieksza niz 90
        powyzej90 += v # to dodajemy jej wartosc (tyle ile razy sie powtarza

print(powyzej90)
# print(len(pary))

# Zadanie 3.2.

wszystkie_pary = {}
for i in range(10): # i = pierwsza liczba
    # wszystkie_pary[i] = 0
    for j in range(10):
        para = str(f"{i}{j}")
        wszystkie_pary[para] = 0
#od nowa resetujemy tabele

# robimy pary z wszysktich mozliwych kombinacji czyli te nasze + 00 01
pary_z_wszystkimi: dict[str, int] = wszystkie_pary

for i in range(len(znaki)-1):
    znaki[i], znaki[i+1] = znaki[i].strip(), znaki[i+1].strip()

    para = str(f"{znaki[i]}{znaki[i+1]}")

    pary_z_wszystkimi[para] += 1


najmniejsza_k = ''
najmniejsza_v = 999 # początkowa wysoka aby znalezc mniejsza
najwieksza_k = ''
najwieksza_v = 0
print(pary_z_wszystkimi)
for k, v in pary_z_wszystkimi.items():
    # print(k,v)


    if v > najwieksza_v: # jesli wartosc danej jest wieksza od najwiekszej
        najwieksza_v = v
        najwieksza_k = k
    elif v < najmniejsza_v: # jesli wartosc jest mniejsza niz najmniejsza to ja ustaw
        najmniejsza_k = k
        najmniejsza_v = v


print("Najmniejsza")
print(najmniejsza_k,najmniejsza_v)
print("Najwieksza")
print(najwieksza_k,najwieksza_v)


# Zadanie 3.3.

# ciągi 6 cyfrowe ciagi rosnaco malejace

# for plik.readlines() as plik:

plik = open('pi.txt', 'r')
# plik = open('pi_przyklad.txt', 'r')
dlugosc_ciagu = 6
grupy = []

liczby = ''

for liczba in plik.readlines():
    liczba = liczba.strip()
    liczby += liczba


for i in range(len(liczby)-5):
    grupa = liczby[i:i+6]
    # print(grupa)
    grupy.append(grupa)

# print(grupy)

ciagi_rosnaco_malejace = []
for ciag in grupy:
    ciag_rosnacy = ciag[:3]
    ciag_malejacy = ciag[3:]
    # print(ciag_rosnacy)
    # print(ciag_malejacy)
    jest_rosnacy:bool = ciag_rosnacy[0] <= ciag_rosnacy[1] <= ciag_rosnacy[2]
    # print(jest_rosnacy)
    jest_malejacy: bool = ciag_malejacy[0] >= ciag_malejacy[1] >= ciag_malejacy[2]
    # print(jest_rosnacy)
    if jest_rosnacy and jest_malejacy: # jeśli jest rosnący do połowy i malejacy od polowy
        ciagi_rosnaco_malejace.append(int(ciag))

print(len(ciagi_rosnaco_malejace))