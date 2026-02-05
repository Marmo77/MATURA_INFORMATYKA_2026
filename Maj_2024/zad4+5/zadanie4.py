

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


linia1: list[int] = linie[0].strip().split(" ") # dzielniki
linia2: list[int] = linie[1].strip().split(" ") # liczby

print(linia2)







# zad 5

# 1. F
# 2. F
# 3, P