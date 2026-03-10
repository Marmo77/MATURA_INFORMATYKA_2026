# https://arkusze.pl/maturalne/informatyka-2025-czerwiec-matura-rozszerzona.pdf - arkusz
# liczba_przyklad = 3487 # liczba parzysta zawsze parzysta czyli:  MOŻE: 1234 dlugosc = 4| NIE MOŻĘ: 12345 dlugosc = 5 | dlugosc musi być parzysta
import math

def pociecie_na_pol(liczba: int):
    polowa_dlugosci = len(str(liczba)) // 2

    pierwsza_p = str(liczba)[:polowa_dlugosci] #od początku do polowy
    druga_p = str(liczba)[polowa_dlugosci:] #od połowy do końca

    pierwsza_p = int(pierwsza_p) #na liczbe konwersja
    druga_p = int(druga_p) #na liczbe konwersja
    return pierwsza_p, druga_p


plik = open("liczby1.txt", "r")
spelniaja_warunek = 0
for linia in plik.readlines():
    k: int = int(linia.strip())

    a,b = pociecie_na_pol(k)

    # print(a,b)

    print(math.gcd(a,b))

    wynik_nwd = math.gcd(a,b)
    if wynik_nwd == 1:
        print(f"Liczba {k} jest połowicznie względnie pierwsza, ponieważ największy wspólny dzielnik liczb {a} i {b} jest równy {wynik_nwd}")
        spelniaja_warunek += 1
    else:
        print(f"Liczba {k} nie jest połowicznie względnie pierwsza, ponieważ największy wspólny dzielnik liczb {a} i {b} jest równy {wynik_nwd}")
print(f"Liczby spełniające warunek: {spelniaja_warunek}")

with open("wyniki2_2.txt", "w") as f:
    f.write(str(spelniaja_warunek))
# spełniają warunek dla liczby1.txt : 296