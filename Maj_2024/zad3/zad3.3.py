import math

def niparzysty_skrot(liczba: int):
    wynik = 0
    c = 1
    for i in range(len(str(liczba)), 0, -1): # musimy isc od tylu zeby wynik np. z liczby n1 wyszedl 97 a nie 79 bo wtedy idziemy od lewej -> a nie od od tylu | zeby to zrobic ze od 0 do len(liczba) to wtedy bysmy musieli c zmniejszac a nie wiekszac
        akt_liczba = str(liczba)[i-1]
        
        akt_liczba = int(akt_liczba)
        
        if akt_liczba % 2 != 0:
            wynik = wynik + akt_liczba * c
            c = c * 10
    
    return wynik

plik = open("skrot2.txt", "r")

for wiersz in plik.readlines():
    liczba = wiersz.strip()
    liczba = int(liczba)
    # print(liczba)
    
    wynik_npskrot = niparzysty_skrot(liczba=liczba)
    # print(wynik_do_nwd)
    nwd_np = math.gcd(wynik_npskrot, liczba) # najwiekszy wspolny dzielnik liczby i jej nieparzystego skrotu 
    
    if nwd_np == 7: # jesli jest rowny 7 to wypisz
        print(liczba)
    