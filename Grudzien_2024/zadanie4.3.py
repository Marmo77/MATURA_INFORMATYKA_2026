with open("prostokaty.txt", "r") as f:
    plik = f.readlines()


    his = []
    for line in plik:
        line = line.strip()
        h,s = line.split(" ")
        h,s = int(h),int(s)
        his.append([h,s])

    kazda_wysokosc = {}
    for h,s in his:
        if h not in kazda_wysokosc:
            kazda_wysokosc[h] = []

        kazda_wysokosc[h].append(s)
    najw2 = []
    najw3 = []
    najw5 = []
    for i in kazda_wysokosc.values():
        posortowana = sorted(i)[::-1]
        if len(posortowana) > 1:
            dwanajwieksze = posortowana[0] + posortowana[1]
            najw2.append(dwanajwieksze)
        if len(posortowana) > 2:
            trzynajwieksze =  posortowana[0] + posortowana[1] + posortowana[2]
            najw3.append(trzynajwieksze)
        if len(posortowana) > 4:
            piecnajwiekszych = posortowana[0] + posortowana[1] + posortowana[2] + posortowana[3] + posortowana[4]
            najw5.append(piecnajwiekszych)
    dla2prostokatow_najw = max(najw2)
    dla3prostokatow_najw = max(najw3)
    dla5prostokatow_najw = max(najw5)
    print(dla2prostokatow_najw)
    print(dla3prostokatow_najw)
    print(dla5prostokatow_najw)

    # print(kazda_wysokosc)






