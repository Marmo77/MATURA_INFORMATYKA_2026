#2.3 najwieksza
plik = open("symbole_przyklad.txt", "r")
# o = 0
# + = 1
# * = 2

najwyzszy_wynik = -1
najwyzszy_wynik_text = ""
wiersze = plik.readlines()

for wiersz in wiersze:
    aktualny_wynik = ""
    wiersz = wiersz.strip()
    
    for znak in wiersz:
        if znak == "o":
            aktualny_wynik += "0"
        elif znak == "+":
            aktualny_wynik += "1"
        elif znak == "*":
            aktualny_wynik += "2"
    #konwersja na dziesietny
    
    odwrocony_wynik = aktualny_wynik[::-1] #odwrocenie aby isc od tylu
    wynik_dziesietny = 0
    for idx,liczba in enumerate(odwrocony_wynik): # dla kazdej liczby mnozyzymy ja razy 3 do potęgi takiej na jakim są indeksie
        # print(idx,liczba)
        wynik_dziesietny += int(liczba) * 3**idx
        
    
    if wynik_dziesietny > najwyzszy_wynik:
        najwyzszy_wynik = wynik_dziesietny
        najwyzszy_wynik_text = wiersz

print(f"{najwyzszy_wynik} {najwyzszy_wynik_text}")


# 2.4

suma_wynikow_pliku = 0
suma_wynikow_pliku_text = ""

for wiersz in wiersze:
    aktualny_wynik = ""
    wiersz = wiersz.strip()
    
    for znak in wiersz:
        if znak == "o":
            aktualny_wynik += "0"
        elif znak == "+":
            aktualny_wynik += "1"
        elif znak == "*":
            aktualny_wynik += "2"
            
    # konwersja na dziesietny, poprzez int
    
    wynik_dziesietny = int(aktualny_wynik,3)
    suma_wynikow_pliku += wynik_dziesietny # dla kazdego wiersza obliczamy ile wynosi wynik dziesietny i go dodajemy do wyniku calego pliku
    

#trzeba teraz sume dziesietna przekontwertowac na trojkowy
trojkowy_suma = ""
s = suma_wynikow_pliku
while s > 0:
    trojkowy_suma = str(s%3) + trojkowy_suma # dodawanie do przodu zamist dodac na koniec np. 0 na koniec 10 to dodajemy do przodu 01
    s = s //3 # div mod
    
# print(trojkowy_suma)

# teraz trojkowy na symbole
s_text = suma_wynikow_pliku_text 
for liczba in trojkowy_suma:
    if liczba == "0":
        s_text += "o"
    elif liczba == "1":
        s_text += "+"
    elif liczba == "2":
        s_text += "*"

print(suma_wynikow_pliku, s_text)