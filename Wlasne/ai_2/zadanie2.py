# ZADANIE 2

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
najwieksze_wartosci.append("1111111")
if len(najwieksze_wartosci) > 1 :
    najwieksza_wartosc = max(int(najwieksze_wartosci[i], 2) for i in range(len(najwieksze_wartosci)))
    najwieksza_wartosc = bin(najwieksza_wartosc)[2:]
    print("maks")
else:
    najwieksza_wartosc = int(najwieksze_wartosci[0])

print(najwieksza_wartosc)