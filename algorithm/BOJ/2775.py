T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]

    for x in range(k):
        for y in range(1, n):
            floor[y] += floor[y-1]
    print(floor[-1])




