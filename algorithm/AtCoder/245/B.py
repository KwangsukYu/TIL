N = int(input())

sset = set(map(int, input().split()))

for i in range(N+1):
    if i not in sset:
        print(i)
        break