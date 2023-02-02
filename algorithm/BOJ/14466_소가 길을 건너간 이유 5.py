N, K, B = map(int, input().split())

lst = [1] * N
for _ in range(B):
    n = int(input())
    lst[n-1] = 0

ssum = 0
for j in range(K):
    ssum += lst[j]

i = 1
max_v = ssum
while i + K - 1 < N:
    if ssum >= K:
        break
    ssum += (lst[i+K-1] - lst[i-1])

    if ssum > max_v:
        max_v = ssum
    max_v = max(ssum, max_v)
    i += 1

print(K - max_v)
