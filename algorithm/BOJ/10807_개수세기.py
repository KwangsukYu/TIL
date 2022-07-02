N = int(input())
nums = list(map(int, input().split()))
M = int(input())

cnt = 0
for i in nums:
    if i == M:
        cnt += 1

print(cnt)