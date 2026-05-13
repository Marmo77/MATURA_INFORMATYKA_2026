with open("liczby.txt", "r") as f:
    plik = f.readlines()
    liczba_kwadratow = 0
    kwadraty = []
    for line in plik:
        line = line.strip()

        liczba = int(line)
        pierwiastek = int(liczba**0.5)
        # print(liczba,pierwiastek)
        if pierwiastek*pierwiastek == liczba:
            liczba_kwadratow += 1
            kwadraty.append(liczba)

    print(liczba_kwadratow,kwadraty[0])

