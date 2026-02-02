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
