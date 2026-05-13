with open("anagram.txt", "r") as f:
    plik = f.readlines()
    nie_wystepuje_zero = 0

    najwieksza_suma_roznych = 0
    najwieksza_z_roznych = 0

    for line in plik:
        line = line.strip()
        rozne_cyfry = []

        dziesietna = int(line,2)
        dziesietna = str(dziesietna)
        ma_zero = False
        for i in dziesietna:
            if int(i) not in rozne_cyfry:
                rozne_cyfry.append(int(i))
            if i == "0":
                ma_zero = True
        if ma_zero == False:
            nie_wystepuje_zero += 1

        suma = 0
        for liczba in rozne_cyfry:
            suma += liczba
        if suma > najwieksza_suma_roznych:
            najwieksza_suma_roznych = suma
            najwieksza_z_roznych = int(dziesietna)
    print(nie_wystepuje_zero)
    print(najwieksza_z_roznych)

