N = int(input())
cars = list(map(int, input().split()))

cnt = 0
for i in cars:
    if i == N:
        cnt += 1

print(cnt)