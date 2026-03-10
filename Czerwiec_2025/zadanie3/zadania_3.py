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