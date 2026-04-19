#ODBICIA funkcja
def odbicie(liczba):
    odbita = str(liczba)[::-1]
    return int(odbita)

# print(odbicie(9102))

# Zadanie 4.1.


with open("liczby.txt") as file:
    liczby = file.readlines()
    podzielne_przez_17 = []
    for liczba in liczby:
        liczba = int(liczba.strip())
        odbita = odbicie(liczba)
        # print(f"liczba : {liczba}, odbita : {odbita}")
        if odbita % 17 == 0:
            # print("PODZIELNA")
            podzielne_przez_17.append(odbita)

    print(podzielne_przez_17)

# Zadanie 4.2.
print("-----------------------------")

with open("liczby.txt") as file:
    liczby = file.readlines()
    najwieksza_liczba_roznicy = 0
    najwieksza_roznica = 0
    for liczba in liczby:
        liczba = int(liczba.strip())
        odbita = odbicie(liczba)
        # print(liczba, odbita)
        roznica = abs(liczba - odbita)
        # print(roznica)
        if roznica > najwieksza_roznica:
            najwieksza_liczba_roznicy = liczba
            najwieksza_roznica = roznica

    print(f"NAJWIĘKSZA\n{najwieksza_liczba_roznicy} {najwieksza_roznica}")


# Zadanie 4.3.

print("----------------------------")

def isPrime(liczba):
    if liczba <= 1:
        return False
    if liczba <= 3:
        return True
    if liczba % 2 == 0 or liczba % 3 == 0:
        return False
    i = 5
    while i * i <= liczba:
        if liczba % i == 0 or liczba % (i+2) ==0:
            return False
        i += 6
    return True

with open("liczby.txt") as file:
    liczby = file.readlines()
    pierwsze_z_liczbami_i_odbiciami = []
    for liczba in liczby:
        liczba = int(liczba.strip())
        odbita = odbicie(liczba)
        l_prime = isPrime(liczba)
        o_prime = isPrime(odbita)

        if l_prime and o_prime:
            pierwsze_z_liczbami_i_odbiciami.append(liczba)

    print(pierwsze_z_liczbami_i_odbiciami)


# Zadanie 4.4.

print("----------------------------")

with open("liczby.txt") as file:
    liczby = file.readlines()
    slownik = {}
    for liczba in liczby:
        liczba = int(liczba.strip())

        if liczba not in slownik:
            slownik[liczba] = 1
        else:
            slownik[liczba] += 1
    # print(slownik)
    #rozne liczby
    rozne_liczby = 0
    for liczby in slownik:
        rozne_liczby += 1

    #powtarzaja sie
    powtarzaja_sie_2_razy = 0
    powstarzaja_sie_3_razy = 0

    for powtorzenia in slownik.values():
        if powtorzenia == 2:
            powtarzaja_sie_2_razy += 1
        if powtorzenia == 3:
            powstarzaja_sie_3_razy += 1

    print(rozne_liczby, powtarzaja_sie_2_razy, powstarzaja_sie_3_razy)