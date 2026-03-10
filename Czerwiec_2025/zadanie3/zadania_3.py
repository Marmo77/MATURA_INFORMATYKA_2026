# --------------------- ZADANIE 3.1. ---------------------

liczby: list[str] = []
plik = open("dane.txt", "r")
for ciag in plik.readlines():
    ciag = ciag.strip()

    aktualna_liczba = ""
    for idx, znak in enumerate(ciag):
        if znak.isdigit(): #jesli jest int
            aktualna_liczba += znak
            # print(aktualna_liczba)
        else:
            if aktualna_liczba != "": # jesli nie jest pusty (czyli ma 1 lub wiecej)
                liczby.append(aktualna_liczba)
                aktualna_liczba = ""

        #dla ostatniej liczby która zamyka pętle (jesli jest taki przypadek
        if idx == (len(ciag)- 1):
            if aktualna_liczba.isdigit():
                liczby.append(aktualna_liczba)


    # print(liczby)

liczby_start_str_50 = 0
for liczba in liczby:
    liczba_str = str(liczba)
    # print(liczba_str)
    if liczba_str.startswith("50"):
        liczby_start_str_50 += 1
print(f"Zaczynają się od 50 początek: {liczby_start_str_50}")

# with open("wyniki3_1.txt", "w") as f:
#     f.write(f"Wynik dla 3.1:\n{liczby_start_str_50}")


# --------------------- ZADANIE 3.2. ---------------------

# print(liczby)

ilosc_powtorzen: dict[int,int] = {}
for liczba in liczby:
    # print(liczba)
    powtorzenia = 0
    for cyfra in str(liczba):
        cyfra = int(cyfra)
        if cyfra not in ilosc_powtorzen: # jesli nie jest w slowniku to dodajemy i ustawiamy na wartosc 1
            ilosc_powtorzen[int(cyfra)] = 1
        else: # jesli juz jest w slowniku to dopisujemy +1 do wartosci
            ilosc_powtorzen[int(cyfra)] += 1

# print(ilosc_powtorzen)
najwieksza_cyfra = 0
najwiecej_powtorzen = 0
for cyfra, powtorzenia in ilosc_powtorzen.items():
    if powtorzenia > najwiecej_powtorzen:
        najwiecej_powtorzen = powtorzenia
        najwieksza_cyfra = cyfra
print(f"Największa liczba powtórzeń to {najwiecej_powtorzen} dla cyfry {najwieksza_cyfra}")
# print(najwieksza_cyfra,najwiecej_powtorzen)

# --------------------- ZADANIE 3.3. ---------------------

numery_telefonow: list[str] = []

for numer in liczby:
    if len(numer) == 9:
        numery_telefonow.append(numer)

numery_telefonow_na_5 = []

for numer in numery_telefonow:
    if numer.startswith("5"):
        numery_telefonow_na_5.append(numer)

# print(numery_telefonow_na_5)

# with open("wyniki3_3.txt", "w") as f:
#     for numer in numery_telefonow_na_5:
#         f.write(f"{numer}\n")


# --------------------- ZADANIE 3.4. ---------------------


zbiory_roznych = {}
for numer in numery_telefonow:
    rozne: dict[int,int] = {}
    for cyfra in str(numer):
        cyfra = int(cyfra)
        if cyfra not in rozne:
            rozne[cyfra] = 1
        else:
            rozne[cyfra] += 1
    # print(rozne)
    zbiory_roznych[numer] = rozne
# print(numery_telefonow)
# print(zbiory_roznych)

# teraz sprawdzic ktore maja najmniej keys
najkrotsze_zbiory = []
dlugosc_najkrotszego_zbioru = 9999
for zbiory_roznych in zbiory_roznych.items():

    numer = zbiory_roznych[0]
    wartosci = zbiory_roznych[1]
    dlugosc_wartosci = len(wartosci)

    if dlugosc_wartosci < dlugosc_najkrotszego_zbioru: # jesli aktualna dlugosc wartosci jest mniejsza niz poprzednia najwieksza to ja zastepujemy
        dlugosc_najkrotszego_zbioru = dlugosc_wartosci
        najkrotsze_zbiory = [] # nowa wartosc najmnijeszych jest ustanowiona wiec czyscimy najdluzszy ciag
    if dlugosc_wartosci == dlugosc_najkrotszego_zbioru:
        najkrotsze_zbiory.append([numer, dlugosc_wartosci]) # dodajemy do akutalnych numerów liczby takiej samej dlugosci wartosci jak najkroszy zbior


print(dlugosc_najkrotszego_zbioru)
print(najkrotsze_zbiory)