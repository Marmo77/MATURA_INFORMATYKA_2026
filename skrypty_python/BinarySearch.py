
# ! DZIAŁA TYLKO NA !POSORTOWANEJ TABLICY! !!!

tablica = [3,9,12,41,61,82,99]

def szukanieBinarne(tablica, dlugosc_tablicy, szukana_liczba):

    lewy = 1 #skrajny lewy element tablicy
    prawy = dlugosc_tablicy # skrajny prawy element tablicy

    while lewy <= prawy:
        srodek = (prawy + lewy) // 2 # bierzemy srodkowy element -(srednia arytm. i dzielenei calkowite) dla 9 elementow (9+1) // 2 = 5 srodkowy element to 5

        if tablica[srodek] == szukana_liczba:
            return srodek # zwracamy index srodka

        if tablica[srodek] < szukana_liczba: #nasza liczba jest wiekszy od srodkowego elementu to zmniejszamy obszar poszukiwań
            lewy = srodek + 1#o polowe, czyli przesuwamy lewą strone tablicy do srodkowego elementu + 1 (bo wiemy ze obecny srodek nie jest tez rozwiazaniem)
        else: #jesli liczba srodkowa jest > szukanej to prawą strone przysuwamy do srodka -1
            prawy = srodek - 1

    return -1 # jeśli nie znalezlismy liczby

index_szukanej = szukanieBinarne(tablica,len(tablica),41)

print(f"index: {index_szukanej}, szukana: {tablica[index_szukanej]}")