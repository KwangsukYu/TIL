N, M = map(int, input().split())
listen = set()
for i in range(N):
    listen.add(input())
see = set()
for j in range(M):
    see.add(input())

ans = sorted(listen&see)
print(len(ans))
for i in ans:
    print(i)