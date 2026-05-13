with open("prostokaty.txt", "r") as f:
    plik = f.readlines()

    ciag = []

    ciagi_ciagow = []
    for i in range(1, len(plik)):
        line = plik[i].strip()

        h,s = line.split(" ")
        h,s = int(h),int(s)

        poprzedni_h, poprzedni_s = plik[i-1].split(" ")
        poprzedni_h, poprzedni_s = int(poprzedni_h),int(poprzedni_s)
        print((h,s), (poprzedni_h, poprzedni_s))

        if s <= poprzedni_s and h <= poprzedni_h:
            # print("WIEKSZE")
            ciag.append((h,s))
        else:
            ciagi_ciagow.append(ciag)
            ciag = []
            # print("przerwa")
    print(ciagi_ciagow)
    najdluzszy_ciag = 0
    najdluzsza_len_ciagu = 0
    for ciag in ciagi_ciagow:
        dlugsosc = len(ciag)
        print(dlugsosc)
        if dlugsosc > najdluzsza_len_ciagu:
            najdluzsza_len_ciagu = dlugsosc
            najdluzszy_ciag = ciag

    print(najdluzsza_len_ciagu+1, najdluzszy_ciag[-1])


