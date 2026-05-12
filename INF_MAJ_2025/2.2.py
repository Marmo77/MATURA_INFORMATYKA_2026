plik = open("symbole_przyklad.txt","r")


linie = plik.readlines()

for i in range(0,len(linie)-2):

    linia1 = linie[i].split()
    linia2 = linie[i+1].split()
    linia3 = linie[i+2].split()
    print(linia1)
    print(linia2)
    print(linia3)
    print("--------")
    #tak zrobic aby sprawdzac 3x3 dla kazdej lini musimy 3 elementy
    for j in range(0,len(linia1)-2):
        znakX1 = linia1[j]
        znakX2 = linia1[j+1]
        znakX3 = linia1[j+2]
        print(znakX1, znakX2, znakX3)



