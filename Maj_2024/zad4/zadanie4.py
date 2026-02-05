

plik = open("liczby_przyklad.txt", "r")
linie = plik.readlines()

linia1: list[int] = linie[0].strip().split(" ") # dzielniki
linia2: list[int] = linie[1].strip().split(" ") # liczby


#zadanie 4.1.


ile_razy_dzielnik = 0
for dzielnik in linia1:
    for liczba in linia2:
        # dla każdego dzielnika sprawdzamy czy jest podzielny przez liczbę
        if int(liczba) % int(dzielnik) == 0:
            # print("jest dzielnikiem")
            ile_razy_dzielnik += 1
            break # jeśli jest dzielnikiem to przechodzimy do następnego dzielnika (przerywamy pętle dla tej liczby bo znaleźliśmy dla niej liczbę podzielną)

print(f"Dzielone są: {ile_razy_dzielnik}")
            
            
            
#zadanie 4.2.
posortowana = linia1
# posortowana.sort() # mozna tak posortowac


#albo tak posortowac np
for i in range(len(posortowana)):
    for j in range(0, len(posortowana) - 1 - i):
        if int(posortowana[j]) < int(posortowana[j+1]): # jeśli pierwsza jest wieksza od tej stylu to zamien miejscami
        # w zadaniu jest od najwiekszej do najmniejszej wiec znak w porownaniu '<' pierwsza jest mniejsza od drugiej to podmien
            posortowana[j], posortowana[j+1] = posortowana[j+1], posortowana[j] #podmianka
            
# print(posortowana)

liczba_w_kolejnosci = posortowana[100] # 101 liczbą czyli index 100 bo jest liczony od 0 czyli 101 element od 0 do 100 to 101 elementow

print(liczba_w_kolejnosci)

print("-----------")
#zadanie 4.3.

mozna_obliczyc: list[int] = []

for i in range(len(linia2)): #dla kazdej liczby calkowietej
    liczba_przed_zmianami = linia2[i] # trzeba takie dodać bo inaczej ta liczba zostanie zmodyfikowana na 1 i wynik będzie 1
    
    for j in range(len(linia1)): # przechodzimy przez wszystkie dzielniki
        if int(linia2[i]) % int(linia1[j]) == 0: # jesli nasza liczba calkowita po dzieleniu przez dzielnik da 0 czyli się przez nią dzieli
            linia2[i] = int(linia2[i]) / int(linia1[j]) # to zmniejszamy naszą liczbę o wartość z dzielenia
    # po zakończeniu dzielenia l.całkowitej jeśli wynik z dzielenia 1 czyli jest w stanie się przez nie dzielić to dodajemy do tablicy z liczbami (uzywamy liczby pomocniczej przed zmianami, poniewaz jesli teraz dodamy zwykla to bedize wynosila 1)
    if linia2[i] == 1:
        mozna_obliczyc.append(int(liczba_przed_zmianami))
        
        
# print(mozna_obliczyc)
print(", ".join(str(liczba) for liczba in mozna_obliczyc))

#zadanie 4.4.


# linia1: list[int] = linie[0].strip().split(" ") # dzielniki
# linia2: list[int] = linie[1].strip().split(" ") # liczby

print(linia2)


# ----------------------------  
# wystapienia: dict[int, int] = {}

# # zliczamy ile razy występują w tekscie
# for liczba in linia1:
#     liczba = int(liczba)
#     # print(liczba)
#     wystapienia[liczba] = wystapienia.get(liczba, 0) +1
#     # wypisuje wystąpienia
# # print(wystapienia) 

# # elminujemy te co jest < mninej niż 50

# jedyne_mozliwe = []

# for klucz, wartosc in wystapienia.items():
    
#     if wartosc >= 50:
#         jedyne_mozliwe.append(klucz)

# print(jedyne_mozliwe) # zmniejszamy zakres szukanych liczb tylko do takich ktore wystepują min. 50 razy w lini1

# to działa tylko dla elementów a nie ich fragmentow :(
    
# tutaj miałem błedne myślenie myślałem że chodzi o to że wspólne elementy to takie które są takie same czyli np liczba 5 wystepuje w liczby_przyklad.txt 50 razy to srednia z niej ale to nie ma sensu bo to zawsze jest 5 :D

# ----------------------------  

# ----------------------- nowe podejście: -----------------------
# sprawdzamy sume każdych następnych elementów w grupach 50 czyli od index 0 do 49 i jego średnia
# pozniej 1 - 50 i srednia i tak wszystkie elementy do konca tablicy - 49 bo ostatni fragment to od len(tablicy)-49 do jej dlugosci i zlicza srednia, z tych wszystkich bierzemy największą srednia i sprawdzamy czy da się dodać ewentualnie kolejny element i zobaczyc czy srednia sie zwieksza jesli tak to dodajemy i sprawdzamy nastepny do poki srednia nie bedize mniejsza od poprzedniej :D

liczbyPierwsze = list(map(int, linie[0].strip().split(" ")))
# print(liczbyPierwsze)

max_srednia = 0
cala_tablica_max = []
zakres_sredniej: list[int, int] = 0, 0
for i in range(len(liczbyPierwsze)-49):
    tablica_ze_srednimi = []
    for j in range(i, i+50,1): # liczmy od zakresu i do i +50, czyli 50 elementów listy od 0-49, 1-50, 2-51 i tak każdy zliczamy
        tablica_ze_srednimi.append(liczbyPierwsze[j])
    
    srednia = sum(tablica_ze_srednimi) / len(tablica_ze_srednimi)
    # print(srednia)
    if srednia > max_srednia:
        max_srednia = srednia
        cala_tablica_max = tablica_ze_srednimi
        zakres_sredniej = [i, i+50]
        
# mając już ten najlepszy teraz bedziemy sprawdzać czy jeśli nie dodamy następnego elementu to srednia nie urosnie, jesli nie to jest nasz maksymalny zakres, jesli tak to zmieniamy 
print(f"Największa srednia dla liczby 50 elementów: {max_srednia}")
print(f"Liczba elementów: {len(cala_tablica_max)}")
print(f"Początkowa liczba: {cala_tablica_max[0]}")
# dziala tylko dla 50 elementów a nie jesli jest wieksza grupa, dziala przy zalozeniu ze najwieksza dlugosc bedzie 50

