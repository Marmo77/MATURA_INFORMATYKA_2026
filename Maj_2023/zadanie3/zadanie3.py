
plik = open('pi.txt', 'r')


# Zadanie 3.1.

# - trzeba znaleźć wszystkie dwuszyfrowe
# - przechodzimy przez kazdy element czyli przez range dlugosci -1

znaki = plik.readlines()

pary: dict[int, int] = {} # lista wszystkich par
for i in range(len(znaki)-1):
    znaki[i], znaki[i+1] = znaki[i].strip(), znaki[i+1].strip()

    para = str(f"{znaki[i]}{znaki[i+1]}")
    para = int(para)
    if para in pary:
        pary[para] += 1
    else:
        pary[para] = 1

print(pary)
powyzej90 = 0
for k, v in pary.items(): # przez kazdą pare przechodzimy
    if k > 90: # jeśli klucz czyli liczba wieksza niz 90
        powyzej90 += v # to dodajemy jej wartosc (tyle ile razy sie powtarza

print(powyzej90)

# print(d)

