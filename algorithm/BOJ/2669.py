arr = [[0 for i in range(100)]for i in range(100)]
for squ in range(4):
    a, b, c, d = map(int, input().split())
    for x in range(a, c):
        for y in range(b, d):
            arr[x][y] = 1

cnt = 0
for i in arr:
    for j in i:
        if j:
            cnt += 1
print(cnt)


