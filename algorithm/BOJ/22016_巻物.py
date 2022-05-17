N, K = map(int, input().split())
T = list(input())

for i in range(K-1, N):
    if T[i].isupper():
        T[i] = T[i].lower()
    else:
        T[i] = T[i].upper()

print(''.join(T))