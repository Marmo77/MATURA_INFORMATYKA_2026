
#2.1
# co musimy zrobić ?
# - liczbe zwykłą przekształcić na binarną
# - sprawdzać czy następny znak jest taki sam jak poprzedni
# - jeśli jest inny to znaczy że zaczynamy inny blok


przykladowa_liczba: int = 245

def przeksztalc_na_binarna_i_policz_bloki(liczba: int) -> int:
    binarna = 0
    mnoznik = 1
    b = 0 # bloki

    while liczba > 0:
        reszta = liczba % 2 # pokazuje reszte z binarnej
        # print(reszta)
        binarna = binarna + reszta * mnoznik
        mnoznik = mnoznik * 10 # zeby nastepna petla dodawała do przed a nie z tylu

        # print(f"r: {reszta}, {liczba // 2 % 2}")
        r, n = reszta, liczba // 2 % 2 # bierzemy aktualną resztę i porównujemy ją z następną czyli połową liczby z dzielenia % 2 jeśli są rózne to znaczy ze sie zaczął nowy blok
        if r != n:
            b+= 1 # zwiększamy bloki gdy nie są one takie same jak następna liczba
        liczba = liczba // 2 # na koniec działania dzieli ją przez 2 bez reszty (reszte wpisujemy w binarny)

    # print(binarna)
    return b # b = bloki

# liczba1 = przeksztalc_na_binarna_i_policz_bloki(przykladowa_liczba)

# print(liczba1)

def przeksztalc_na_dziesietne(binarna: int):
    liczba = 0
    potega = 0

    while binarna > 0:
        bit = binarna % 10
        # print(bit)
        liczba += bit * (2 ** potega)
        potega += 1
        binarna = binarna // 10

    return liczba

# print(przeksztalc_na_dziesietne(101101))

plik = open("bin.txt", "r")

# zadanie 2.2.


bloczki = 0
for wiersz in plik.readlines():

    wiersz = wiersz.strip()
    liczba = przeksztalc_na_dziesietne(int(wiersz))
    # print(wiersz)
    # print(liczba)
    bloki = przeksztalc_na_binarna_i_policz_bloki(liczba)
    # print(bloki)
    if bloki <= 2:
        bloczki += 1

print(f"Liczba bloków: {bloczki}")

# Zadanie 2.3.


plik = open("bin.txt", "r")

najwieksza = 0
binarna_najwiekszej = 0
for wiersz in plik.readlines():
    wiersz = wiersz.strip()

    liczba_binarna = wiersz

    dziesietna = przeksztalc_na_dziesietne(int(liczba_binarna))

    if dziesietna > najwieksza:
        najwieksza = dziesietna
        binarna_najwiekszej = liczba_binarna


print(binarna_najwiekszej)

# Zadanie 2.4.

#- Zdjęcie

# Zadanie 2.5.

plik = open("bin.txt", "r")

zapisz_wynik = open("wyniki2_5.txt", "w")
# w zadaniu trzeba:
# liczbe binarna na dziesietna przekonwertowac
# p div 2 = liczba dziesietna / 2 = int w dol zaokraglony
# pozniej ja znowu przekonwertowac na binarne

# i zrobić XOR

def bin_na_dziesietna(binarna: str):
    return int(binarna, 2)


for wiersz in plik.readlines():
    liczba = wiersz.strip()

    p_dziesietne = bin_na_dziesietna(liczba)

    # print(p_dziesietne)

    p: int = p_dziesietne

    p_div: int = p // 2


    # print("-------------")


    # print(p, p_div)

    p_bin = bin(p)[2:]
    p_bin_div = bin(p_div)[2:]
    # print(p_bin, p_bin_div)

    # odwracamy i porownujemy kazdy z kazdym jesli wedlug zasad XOR i podmieniamy

    wynik_XOR = ''
    pozostalosci_niezmieniane = ''
    leng_p = 0
    if len(p_bin) > len(p_bin_div):
        leng_p = len(p_bin_div)
        # print("rozmiar:")
        pozostalosci_niezmieniane += p_bin[:-leng_p]
        # print(wynik_XOR)
        # print("------")
    else:
        leng_p = len(p_bin)
        wynik_XOR += p_bin[:-leng_p]
    # print(leng_p)

    #przechodzimy przez krotszy a w dlozszym nie zmieniamy

    p_bin_r = p_bin[::-1]
    p_bin_div_r = p_bin_div[::-1]

    # print(p_bin_r,p_bin_div_r)


    for i in range(leng_p):
        p = str(p_bin_r)[i]
        q = str(p_bin_div_r)[i]
        # print(p,q)
        if p == q:
            wynik_XOR += '0'
        else:
            wynik_XOR += '1'
    wynik_XOR = wynik_XOR[::-1]
    wynik_XOR = pozostalosci_niezmieniane + wynik_XOR
    print(wynik_XOR)
    zapisz_wynik.write(wynik_XOR + "\n")
    # wynik_XOR)

