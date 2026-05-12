plik = open("symbole.txt","r")

def na_trojkowy(liczba):
    if liczba == 0:
        return "0"

    digits = []
    while liczba > 0:
        digits.append(str(liczba % 3))
        liczba = liczba // 3

    return "".join(reversed(digits))

liczby = []
for line in plik.readlines():
    line = line.strip()

    liczba_trojkowa = ""
    for char in line:
        if char == "o":
            liczba_trojkowa += "0"
        elif char == "+":
            liczba_trojkowa += "1"
        elif char == "*":
            liczba_trojkowa += "2"
    # print(liczba_trojkowa)
    liczba_na_dziesietny = int(liczba_trojkowa, 3)
    liczby.append(liczba_na_dziesietny)

suma = sum(int(x) for x in liczby)
trojkowy = na_trojkowy(suma)

symbole = ""
for znak in trojkowy:
    if znak == "0":
        symbole += "o"
    if znak == "1":
        symbole += "+"
    if znak == "2":
        symbole += "*"

print(suma,symbole)
