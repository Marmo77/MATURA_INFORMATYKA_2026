# ZADANIE 2
from cmath import sqrt

# 2.1.


liczby = {}
with open("liczby.txt", "r") as f:
    for l in f.readlines():
        ciag = l.strip()
        # print(l)
        if ciag not in liczby:
            liczby[ciag] = 0
        for cyfra in ciag:
            if cyfra == "1":
                liczby[ciag] += 1
    # liczby = sorted(liczby, reverse=True)
    # print(liczby)

najwieksze_wartosci = []
najwieksza_wartosc = 0
najwieksza_w = 0
for liczba,wartosc in liczby.items():
    # print(liczba, wartosc)
    if wartosc > najwieksza_w:
        najwieksze_wartosci = []
    if wartosc >= najwieksza_w:
        najwieksza_w = wartosc
        najwieksze_wartosci.append(liczba)

# print(int(najwieksze_wartosci[0], 2))
if len(najwieksze_wartosci) > 1 :
    najwieksza_wartosc = max(int(najwieksze_wartosci[i], 2) for i in range(len(najwieksze_wartosci)))
    najwieksza_wartosc = bin(najwieksza_wartosc)[2:]
else:
    najwieksza_wartosc = int(najwieksze_wartosci[0])

print(f"Największa liczba: {najwieksza_wartosc}")


# 2.2.

def na_dziesietne(binarna) -> int:
    return int(binarna,2)


def SitoErastotelese(n):
    pierwsze = [True for _ in range(n+1)]
    pierwsze[0] = pierwsze[1] = False #0 i 1
    for i in range(2, int(n**0.5)+1):
        if pierwsze[i]:
            for j in range(i*i, n+1,i):
                pierwsze[j] = False

    pierwszeLiczby =[]
    for i in range(len(pierwsze)):
        if pierwsze[i]:
            pierwszeLiczby.append(i)
    return pierwszeLiczby

pierwsze = SitoErastotelese(100)

print(pierwsze)