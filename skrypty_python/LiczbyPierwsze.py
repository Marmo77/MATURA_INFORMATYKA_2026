# zakładamy na start ze kazda liczba jest pierwszą

def liczbyPierwsze(n): # n ilosc elementów
    Pierwsze = [True] * (n+1) # robimy tablice, gdzie wszystkie elementy są True, n+1 bo zaczynamy od 0, wiec jesli n = 25,jak 0-25 to 26 elementow czyli n+1

    #wiemy że 0 i 1 nie są więc je wyrzucamy
    Pierwsze[0], Pierwsze[1] = False, False

    #dla każdego elementu tablicy pierwszego, przechodzimy i wyrzucamy jego wielokrotności
    #zakres od idx = 2 czyli od liczby 2 do pierwiastka z n czyli jestli n = 25, to od 2 do 5 włącznie,
    for i in range(2, int(n**(1/2))+1,1):  #od 2 dla każdego elementu do pierwiastka (int, aby nie był float dla np. pierwiastek(26) = 5,10
        if Pierwsze[i]: #jeśli jeszcze nie przechodziliśmy przez ten element
            for wielokrotnosc in range(i*i, n+1, i): #zaczynajac od wielokrotnosci, czyli dla liczby 2 to 2*2 = 4,
                # przechodzimy az kiedy nie jest wiekszy od naszego n, i co przejscie zwiekszamy wielokrotnosc o liczbe i
                # dla 2 i n=25, start: 4, stop: 26, przejscie: 2, przechodzimy przez wszystkie elementy 4,6,8,10,12,... < 26 i wyrzucamy
                Pierwsze[wielokrotnosc] = False
    # mając tablice w True tylko dla tych co są pierwsze, teraz trzeba zamienić wartości True w liczby
    liczby_pierwsze = []

    for i in range(n+1):
        if Pierwsze[i]: #jeśli pierwsza z tym samym indexem jest True, to jest pierwsza
            liczby_pierwsze.append(i)
    return liczby_pierwsze

print(liczbyPierwsze(25))