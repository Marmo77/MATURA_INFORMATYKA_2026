q = int(input())

for _ in range(q):
    n = int(input())
    s, t = map(list[str], input().split())

    s_sorted = sorted(s)
    t_sorted = sorted(t)
    if s_sorted == t_sorted:
        print("YES")
    else:
        print("NO")