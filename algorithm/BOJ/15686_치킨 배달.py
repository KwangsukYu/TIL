from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
c_location = []
h_location = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            c_location.append((i, j))
        elif arr[i][j] == 1:
            h_location.append((i, j))

c_comb = list(combinations(c_location, M))

def dist(nr, nc, r, c):
    return abs(nr - r) + abs(nc - c)

c_lst = []
for i in range(len(c_comb)):
    h = 0
    for r, c in h_location:
        min_v = 1000000
        for x, y in c_comb[i]:
            d = dist(x, y, r, c)
            if d < min_v:
                min_v = d
        h += min_v

    c_lst.append(h)
c_lst.sort()
print(c_lst[0])
    


