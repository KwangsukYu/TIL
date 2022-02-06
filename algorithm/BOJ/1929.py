M, N = map(int, (input().split()))

a = [True for number in range(N + 1)]
a[1] = False
for i in range(2, int(N**0.5) + 1):
    if a[i] == True:
        j = 2
        while i * j <= N:
            a[i * j] = False
            j += 1

for k in range(M, N + 1):
    if a[k]:
        print(k)

