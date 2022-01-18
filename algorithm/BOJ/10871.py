N, X = input().split()
nlist = list(map(int, input().split()))
result = ''
for i in nlist:
    if i < int(X):
        result = i
        print(result, end=' ')


