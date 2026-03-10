# Założenia
# - wszystkie liczby są pierwsze [True]
# - przechodzimy przez wszystkie liczby od 2 do n
# - wykreslamy wszystkie wielokrotnosci liczby
# - liczba 0 i 1 nie są pierwsze

def sito(n):

    pierwsze = [True] * (n + 1)

    pierwsze[0] = pierwsze[1] = False # liczby 0 i 1 nie są pierwsze

    # print(pierwsze)

    p = 2
    while p * p <= n: # do póki kwadrat z obecnej liczby nie jest większy od podago zakresu np. n = 50 7*7 < 49| 7*8=56 czyli juz nie jest brane pod uwagę

        if pierwsze[p]: # jeśli nie zostało wykreślone
            for i in range(p * p, n + 1, p): # zakres sprawdzania od np. p = 2 n = 30 to:  każda wielokrotność  jest wykreslana czyli 2*2 = 4 wylatuje, i przesuwamy się o p czyli:
                # czyli zakres to od dla p=2 to zakres 2*2 = 4 czyli od 4, do (n + 1) i przesuwamy o p czyli 2 => 4,6,8,10 itd. az do konca i wyrzucamy z liczb pierwszych
                pierwsze[i] = False
        p +=1


    liczbyPierwszeArr = []
    for i in range(2, n +1): # dla kazdej liczby z zakresu
        if pierwsze[i]: # jesli jest pierwszą
            liczbyPierwszeArr.append(i)
            # print(i) # to wypisujemy jej index (czyli liczbę która jest pierwsza
    return liczbyPierwszeArr

# n -> Zakres liczb do sprawdzenia czyli np od 0-100 to n = 100
print(sito(1000))