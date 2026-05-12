plik = open("symbole.txt","r")

liczby_i_wartosci_dzies = {}
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
    liczba_na_dziesietny = int(liczba_trojkowa,3)
    # print(liczba_na_dziesietny)
    liczby_i_wartosci_dzies[line] = liczba_na_dziesietny

# print(liczby_i_wartosci_dzies)
najwiekszaL = 0
najwiekszyC = ""
for item,key in liczby_i_wartosci_dzies.items():
    if key > najwiekszaL:
        najwiekszaL = key
        najwiekszyC = item
print(najwiekszaL, najwiekszyC)