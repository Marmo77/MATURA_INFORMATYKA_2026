# n: int | >= 10
import math

#musimy zrobić takie cięcie w którym każdy przypadek cięcia trzeba rozważyć czyli dlugosc i schodzimy w dol przez kazdy przyklad np. 7921 -> 792, 1 -> 79, 21 -> 7, 921




liczba = (2757**2)
print(liczba)

plik =  open("liczby2.txt", "r")


najwiekszy_stopien_kaprekara = 0
najweksza_liczba_kaprekara = 0
for liczba in plik.readlines():
    liczba = int(liczba.strip())
    liczba_sqr = liczba ** 2
    stopien_kaprekara = 0

    l,p = 0, len(str(liczba_sqr))-1
    # print(f"LICZBA: {liczba} -------")
    liczba_str = str(liczba_sqr)
    for i in range(len(liczba_str)-1):
        a = int(liczba_str[l:p])
        b = int(liczba_str[p:])
        # print(a,b)
        p = p -1

        suma = a + b
        if suma <= liczba:
            # print(f"Jest: {suma}")
            stopien_kaprekara += 1
        # else:
        #     print()
            # print("Nie jest")
    if najwiekszy_stopien_kaprekara < stopien_kaprekara:
        najwiekszy_stopien_kaprekara = stopien_kaprekara
        najweksza_liczba_kaprekara = liczba
    # print(f"Stopien: {stopien_kaprekara}")

print(najwiekszy_stopien_kaprekara)
print(najweksza_liczba_kaprekara)

with open("wyniki2_3.txt", "w") as f:
    f.write(str(najwiekszy_stopien_kaprekara))
    f.write("\n")
    f.write(str(najweksza_liczba_kaprekara))