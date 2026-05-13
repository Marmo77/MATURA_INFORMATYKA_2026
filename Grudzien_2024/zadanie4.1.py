with open("prostokaty.txt", "r") as f:
    plik = f.readlines()

    najmniejsze_pole = 0
    najwieksze_pole = 0
    pola = []
    for line in plik:
        line = line.strip()

        h,s = line.split(" ")
        pole = int(h) * int(s)

        pola.append(pole)

    pola_sort = sorted(pola)

    najmniejsze_pole = min(pola)
    najwieksze_pole = max(pola)
    print(f"Najw: {najwieksze_pole}, Najm: {najmniejsze_pole}")