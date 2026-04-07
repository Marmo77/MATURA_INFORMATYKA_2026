t = int(input())
for _ in range(t):
    square_measures = list(map(int, input().split()))

    if square_measures[0] == square_measures[1] == square_measures[2] == square_measures[3]:
        print("YES")
    else:
        print("NO")

