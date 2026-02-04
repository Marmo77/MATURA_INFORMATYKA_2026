#3.2


# inna metoda na nieparzysta_metode (juz uzywajac funkcji pythona)

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

n1 = 294762
n2 = 39101
print(niparzysty_skrot(n1))
print(niparzysty_skrot(n2))

#3.2

plik = open("skrot.txt", "r")

nie_istniejace_nparz_skroty = []
# nieparzy
for wiersz in plik:
    liczba: int = int(wiersz.strip())
    
    wynik = niparzysty_skrot(liczba=liczba)
    
    if wynik == 0:
        nie_istniejace_nparz_skroty.append(liczba)
    
print(f"Wszystkie liczby nie istniejace w nieparzyste skroty: {len(nie_istniejace_nparz_skroty)}")
print(f"Największa liczba spelniajaca warunek: {max(nie_istniejace_nparz_skroty)}")