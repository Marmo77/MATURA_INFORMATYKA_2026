

plik = open("liczby_przyklad.txt", "r")


#zadanie 4.1.
linie = plik.readlines()

dzielniki: list[int] = linie[0].strip().split(" ")
print(dzielniki)
liczby: list[int] = linie[1].strip().split(" ")
# liczby = liczby.split(" ")
# for dziel in dzielniki:
#     print(int(dziel))
# print(liczby)
ile_razy_dzielnik = 0
for dzielnik in dzielniki:
    for liczba in liczby:
        # dla każdego dzielnika sprawdzamy czy jest podzielny przez liczbę
        if int(liczba) % int(dzielnik) == 0:
            # print("jest dzielnikiem")
            ile_razy_dzielnik += 1
            break # jeśli jest dzielnikiem to przechodzimy do następnego dzielnika (przerywamy pętle dla tej liczby bo znaleźliśmy dla niej liczbę podzielną)

print(f"Dzielone są: {ile_razy_dzielnik}")
            