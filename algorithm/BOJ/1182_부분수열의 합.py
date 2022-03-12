N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1, 1<<N):
    a = []
    for j in range(N):
        if i & (1<<j):
            a.append(lst[j])
    
    if sum(a) == S:
        cnt += 1

print(cnt)



