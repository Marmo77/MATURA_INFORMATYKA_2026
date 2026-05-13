with open("slowa3.txt", "r") as f:

    plik = f.readlines()

    wyraz = [] # n,s,k1,k2
    wyraz.append(int(plik[0].strip()))
    wyraz.append(plik[1].strip())
    k1,k2 = plik[2].strip().split(" ")
    wyraz.append(int(k1))
    wyraz.append(int(k2))
print(wyraz)

def czy_mniejszy(n,s,k1,k2):

    i = k1-1
    j = k2-1
    while i < n and j < n:
        # print(i,j)
        # print(s[i], s[j])

        if s[i] == s[j]:
            i += 1
            j += 1
            # print("przejscie")
        else:
            if s[i] < s[j]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False

n = wyraz[0]
s = wyraz[1]
k1 = wyraz[2]
k2 = wyraz[3]
if czy_mniejszy(n,s,k1,k2) == True:
    print("TAK")
else:
    print("NIE")