plik = open("symbole.txt","r")

palindromy = []
for line in plik.readlines():
    line = line.strip()
    odwrotnie = line[::-1]
    if line == odwrotnie:
        # print("palindrom")
        palindromy.append(line)

print(" \n".join(str(x) for x in palindromy))