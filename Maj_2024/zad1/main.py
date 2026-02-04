# prostokat z 

# n - wierszy
# i
# m - kolumn

# n * m -> liczba pól

# A[1..n][1..m] - opis planszy

# A[i][j] = 0 -> Czarne pole | A[i][j] = 1 -> Białe pole

# [b][c][c] 
# [c][c][c]
# [c][c][b]

# => A[1][1] = 1 | => A[n][m] = 1 | pierwsza oraz prawa dolna jest czarna


# 1.1.

# n to w dol, m w bok
# n = 3, m = 3
# n \/ | m ->
# [b][b][b]
# [c][b][c]
# [b][b][b]
# i = n, j = m
#
# P[1][2] = 0
# P[3][2] = 0
#
# P[3][3] = 1 = P[n][m]
# P[3][3] = P[3][2] lub P[2][3]
# dla kazdego w dol:
    # dla kazdego w linii:
        # Jesli  A[i][j] = 0:
            # P[i][j] = FALSZ
        # inaczej:


# dla

# P[5][3] = 1