def liczbyPierwsze(n):

    Prawdziwe = [True] * (n+1)
    Prawdziwe[0],Prawdziwe[1] = False,False

    for i in range(2, int(n**0.5)+1):
        if Prawdziwe[i]:
            for wielokrotnosc in range(i*i,n+1,i):
                Prawdziwe[wielokrotnosc] = False

    liczby_pierwsze = []
    for i in range(n+1):
        if Prawdziwe[i]:
            liczby_pierwsze.append(i)


    return liczby_pierwsze

with open("liczby.txt", "r") as f:
    plik = f.readlines()
    liczby_z_dziel_ponad5 = []
    for line in plik:
        line = line.strip()
        liczba = int(line)
        dzielniki = 0
        liczby_pierwsze = liczbyPierwsze(liczba+1)
        # print(liczby_pierwsze)
        for dzielnik in liczby_pierwsze:
            if liczba % dzielnik == 0:
                dzielniki += 1
        if dzielniki >= 5:
            liczby_z_dziel_ponad5.append(liczba)
    print(liczby_z_dziel_ponad5)