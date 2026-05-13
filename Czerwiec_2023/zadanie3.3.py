with open("anagram.txt", "r") as f:
    plik = f.readlines()
    print(len(plik)-1)
    najwieksza_roznica = 0
    for i in range(len(plik)-1):
        pierwsza = plik[i]
        sasiad = plik[i+1]
        print(f"{pierwsza}, {sasiad}")
        pierwsza_dz = int(pierwsza,2)
        sasiad_dz = int(sasiad,2)
        roznica = abs(pierwsza_dz - sasiad_dz)
        if roznica > najwieksza_roznica:
            najwieksza_roznica = roznica
    print("-------------")
    print(najwieksza_roznica)
    print(bin(najwieksza_roznica)[2:])



