with open("anagram.txt", "r") as f:
    plik = f.readlines()

    zrownowazone = 0
    prawie_zrownowazone = 0
    for line in plik:
        line = line.strip()
        liczba_jedynek = 0
        liczba_zer = 0
        for i in line:
            print(i)
            if i == "0":
                liczba_zer += 1
            else:
                liczba_jedynek += 1
        print(liczba_jedynek)
        print(liczba_zer)
        if liczba_jedynek == liczba_zer:
            zrownowazone += 1
        elif liczba_jedynek-1 == liczba_zer or liczba_zer-1 == liczba_jedynek:
            prawie_zrownowazone += 1
        else:
            continue
    print("---------")
    print(zrownowazone)
    print(prawie_zrownowazone)

