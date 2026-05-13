with open("liczby.txt", "r") as f:
    plik = f.readlines()

    roznica_wieksza = 0
    roznica_mniejsza = 0
    roznica_rowna = 0
    roznice_rowne_tab = []

    for line in plik:
        line = line.strip()
        liczba = int(line)

        liczba_na_tab = [int(x) for x in str(liczba)]
        najmniejsza_tab = sorted(liczba_na_tab)
        najwieksza_tab = najmniejsza_tab[::-1]


        # print(liczba_na_tab,najmniejsza_tab, najwieksza_tab)

        najmniejsza = 0
        najwieksza = 0
        potega = 1
        for i in range(len(najmniejsza_tab),0,-1): #najmniejsza
            # print(najmniejsza_tab[i-1])
            najmniejsza += najmniejsza_tab[i-1] * potega
            potega = potega * 10
        # print(najmniejsza)

        potega = 1
        for i in range(len(najwieksza_tab), 0, -1):  # najmniejsza
            # print(najwieksza_tab[i - 1])
            najwieksza += najwieksza_tab[i - 1] * potega
            potega = potega * 10
        # print(najwieksza)

        roznica = najwieksza - najmniejsza
        # print(f"r: {roznica}")

        if roznica > liczba:
            roznica_wieksza += 1
        elif roznica < liczba:
            roznica_mniejsza += 1
        elif roznica == liczba:
            roznica_rowna += 1
            roznice_rowne_tab.append(liczba)

    print(f"Roznica wieksza: {roznica_wieksza}")
    print(f"Roznica mniejsza: {roznica_mniejsza}")
    print(f"Roznica taka sama: {roznice_rowne_tab}")